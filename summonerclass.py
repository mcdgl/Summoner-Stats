#imports
import os
import webbrowser
import requests
from requests_html import HTMLSession
from selenium import webdriver
from bs4 import BeautifulSoup #webscraping library

session = HTMLSession()


class Summoner:
    def __init__(self, name = "", region = ""):
        #assigning values passed from main, creating opgg string (target link for webscraping)
        self.region = region
        self.opgg = "https://" + region.lower() + ".op.gg/summoners/" + region.lower() + "/" + name.replace(" ", "%2B")

        print('prior to session')
        r = session.get(self.opgg)
        print('html render')
        r.html.arender()

        print('soup')
        soup = BeautifulSoup(r.html.raw_html, "html.parser")

        #searches to see if the page has the element saying that a user does not exist
        exists = soup.find('h2').text
        if("This summoner is not" in exists):
            print('Summoner does not exist exception')
            raise Exception("HELP I AM TRAPPED IN A PYTHON SCRIPT")
        #we are given a username from the user, but they may have misspelled/capitalized wrong so this ensures spelling etc is same as registered by riot
        self.name = soup.find("span", class_="summoner-name").text
        self.level = soup.find("span", class_="level").text
        #sees if the user is unranked in either solo or flexed
        unranked = soup.findAll("span", class_="unranked")
        print('Searched unranked')
        if unranked:
            for i in unranked: #opgg displays ranked elements in order from ranked solo to flex; if length of i = 2, then i[0] = rankedsolo, i[1] = rankedflex
                if ("Solo" in i.parent.text):#checking parent class which holds "Ranked Solo" or "Ranked Flex"
                    #Setting default values of Unranked and 0 for the sake of displaying info in embed
                    self.soloRank = "Unranked"
                    self.soloLP = '0 LP'
                    self.soloWR = '0% WR'
                if ("Flex" in i.parent.text):
                    self.flexRank = "Unranked"
                    self.flexLP = '0 LP'
                    self.flexWR = 'Win Rate 0%'
        print('Finished unranked checks')
        #checks if the user is ranked in either ranked or flex
        ranked = soup.findAll("div", class_="tier")
        print('Searched ranked')
        #finds all elements displaying user LP, stores as list
        lp = soup.findAll('div', class_='lp')
        print('Searched LP')
        #finds all elements displaying user WinRatio, stores as list
        wr = soup.findAll('div', class_='ratio')
        if ranked:
            for i in range(len(ranked)):
                if ("Solo" in ranked[i].parent.parent.parent.text):#same as before
                    self.soloRank = ranked[i].text.capitalize()#for some reason opgg returns ranks like "master" "challenger" so we just capitalize first letter
                    self.soloLP = lp[i].text
                    self.soloWR = wr[i].text
                if ("Flex" in ranked[i].parent.parent.parent.text):
                    self.flexRank = ranked[i].text.capitalize()
                    self.flexLP = lp[i].text
                    self.flexWR = wr[i].text
        print('Finished ranked checks')

        #find profile picture and return
        print('Finding pfp')
        for i in soup.findAll('img', alt = True): #finding all img elements with alt so we can specifically look for "profile image" alt
            if "profile image" in i['alt']:
                self.pfpLink = i.get('src')
        print(self.pfpLink)
        print('Pfp found')
