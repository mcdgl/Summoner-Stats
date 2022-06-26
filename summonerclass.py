#imports
import os
import webbrowser
import requests
from selenium import webdriver
from bs4 import BeautifulSoup #webscraping library




class Summoner:
    def __init__(self, name = "", region = ""):
        self.name = name
        self.region = region
        self.opgg = "https://" + region.lower() + ".op.gg/summoners/" + region.lower() + "/" + name.replace(" ", "%2B")
        page = requests.get(self.opgg, headers={'User-Agent': 'Mozilla/5.0'}).text
        soup = BeautifulSoup(page, "html.parser")

        #searches to see if the page has the element saying that a user does not exist
        exists = soup.find('h2').text
        if("This summoner is not" in exists):
            raise Exception("HELP I AM TRAPPED IN A PYTHON SCRIPT")
