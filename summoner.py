#imports
import os
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup #webscraping library


class Summoner:
    def __init__(self, name, region):
        self.name = name
        self.region = region
