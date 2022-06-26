#imports
import os
import webbrowser
import requests
from selenium import webdriver
from bs4 import BeautifulSoup #webscraping library


#page = requests.get()

class Summoner:
    def __init__(self, name = "", region = ""):
        self.name = name
        self.region = region
        self.opgg = "https://" + region.lower() + ".op.gg/summoners/" + region.lower() + "/" + name.replace(" ", "%2B")
