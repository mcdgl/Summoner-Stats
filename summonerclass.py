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
        self.region = region
        self.opgg = "https://" + region.lower() + ".op.gg/summoners/" + region.lower() + "/" + name.replace(" ", "%2B")
        #page = requests.get(self.opgg, headers={'User-Agent': 'Mozilla/5.0'}).text

        #session = HTMLSession()
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
        self.name = soup.find("span", class_="summoner-name").text

        #sees if the user is unranked in either rank or flexed
        unranked = soup.findAll("span", class_="unranked")
        print('Searched unranked')
        if unranked:
            for i in unranked:
                if ("Solo" in i.parent.text):
                    self.soloRank = "Unranked"
                    self.soloLP = '0 LP'
                if ("Flex" in i.parent.text):
                    self.flexRank = "Unranked"
                    self.flexLP = '0 LP'
        print('Finished unranked checks')
        #checks if the user is ranked in either ranked or flex
        ranked = soup.findAll("div", class_="tier")
        print('Searched ranked')
        lp = soup.findAll('div', class_='lp')
        print('Searched LP')
        if ranked:
            for i in range(len(ranked)):
                if ("Solo" in ranked[i].parent.parent.parent.text):
                    self.soloRank = ranked[i].text.capitalize()
                    self.soloLP = lp[i].text
                if ("Flex" in ranked[i].parent.parent.parent.text):
                    self.flexRank = ranked[i].text.capitalize()
                    self.flexLP = lp[i].text
        print('Finished ranked checks')
