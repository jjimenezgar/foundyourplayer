#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:03:35 2022

@author: jjimenez
"""

## Extracting Data

import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
To make the request to the page we have to inform the
website that we are a browser and that is why we
use the headers variable
"""
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}



def extract(year,age,page):
    
    
  """
  This function gets the features from a table with the statistics of the best players sub25 in the top football competitions.

  variabes:

  year: Seasson
  age: Player age
  page: Web Page
  
  """

    # page_dir stands for the data page address
    page_dir = "https://www.transfermarkt.co.uk/meisteeinsaetze/topscorer/statistik/2021/art/top10/saison_id/{}/altersklasse/u{}/ausrichtung//spielerposition_id/0/land_id/0/filter/0/plus/3/page/{}".format(year,age,page)
    
    # In the objeto_response variable we will the download of the web page
    objeto_response = requests.get(page_dir, headers=headers)
    
    """
    Now we will create a BeautifulSoup object from our object_response.
    The 'html.parser' parameter represents which parser we will use when creating our object,
    a parser is a software responsible for converting an entry to a data structure.
    """
    pagina_bs = BeautifulSoup(objeto_response.content, 'html.parser')
    
    name_players = [] # List that will receive all the names of the players.
    
    tags_players = pagina_bs.find_all("td",{"class": None})
    # Now we will receive all the cells in the table that have no class atribute set
    
    for tag_player in tags_players:
        # The find() function will find the first image whose class is "bilderrahmen-fixed lazy lazy" and has a title 
      imagem_player = tag_player.find("img", {"class": "bilderrahmen-fixed lazy lazy"}, {"title":True})
        # The imagem_player variable will be a structure with all the image information,
        # one of them is the title that contains the name of the player
      if(imagem_player != None): # We will test if we have found any matches than add them
        name_players.append(imagem_player['title'])
    
    """Player"""
    
    name_players
    
    """Liga"""
    
    competition_players = [] # List that will receive all the names of the competition
    
    tags_players = pagina_bs.find_all("td",{"class": None})
    # Now we will receive all the cells in the table that have no class atribute set
    
    for tag_player in tags_players:
        # The find() function will find the first image whose class is "flaggenrahmen" and has a title
      imagem_player = tag_player.find("img", {"class": "flaggenrahmen"}, {"title":True})
        # The imagem_player variable will be a structure with all the image information,
      if(imagem_player != None): # We will test if we have found any matches than add them
         competition_players.append(imagem_player['title'])
    
    competition_players
    
    """Team"""
    
    team_players = [] # List that will receive all the names of the team
    
    tags_players = pagina_bs.find_all("td",{"class": None})
    # Now we will receive all the cells in the table that have no class atribute set
    
    for tag_player in tags_players:
        # The find() function will find the first image whose class is "tiny_wappen" and has a title
      imagem_player = tag_player.find("img", {"class": "tiny_wappen"}, {"title":True})
        # The imagem_player variable will be a structure with all the image information,
      if(imagem_player != None): # We will test if we have found any matches than add them
        team_players.append(imagem_player['title'])
    
    team_players
    
    """Nationality"""
    
    nationality_players = [] # List that will receive all the nationality players
    
    # The find_all () method is able to return all tags that meet restrictions within parentheses
    tags_players = pagina_bs.find_all("td", {"class": "zentriert"})
    # In our case, we are finding all anchors with the class "spielprofil_tooltip"
    
    for tag_player in tags_players:
        # The find() function will find the first image whose class is "flaggenrahmen" and has a title
      imagem_player = tag_player.find("img", {"class": "flaggenrahmen"}, {"title":True})
        # The imagem_player variable will be a structure with all the image information,
      if(imagem_player != None): # We will test if we have found any matches than add them
        nationality_players.append(imagem_player['title'])
    
    nationality_players
    
    """Age"""
    
    age_players = [] # List that will receive all the players age
    
    # The find_all () method is able to return all tags that meet restrictions within parentheses
    n=25*7
    
    for i in range(1,n,7):
        tags_players = pagina_bs.find_all("td", {"class": "zentriert"})[i]
    # In our case, we are finding all anchors with the class "zentriert"
        for tag_player in tags_players:
          age_players.append(tag_player)
    
    age_players
    
    """Match"""
    
    match_players = [] # List that will receive all the players match
    
    # The find_all () method is able to return all tags that meet restrictions within parentheses
    n=25*7
    
    for i in range(3,n,7):
        tags_players = pagina_bs.find_all("td", {"class": "zentriert"})[i]
    # In our case, we are finding all anchors with the class "zentriert"
        for tag_player in tags_players:
          match_players.append(tag_player.text)
    
    match_players
    
    """Goal"""
    
    goal_players = [] # List that will receive all the players goal
    
    # The find_all () method is able to return all tags that meet restrictions within parentheses
    n=25*7
    
    for i in range(4,n,7):
      tags_players = pagina_bs.find_all("td", {"class": "zentriert"})[i]
        # In our case, we are finding all anchors with the class "zentriert"
      for tag_player in tags_players:
        goal_players.append(tag_player)
    
    goal_players
    
    """Assists"""
    
    Assists_players = [] # List that will receive all the players assists
    
    # The find_all () method is able to return all tags that meet restrictions within parentheses
    n=25*7
    
    for i in range(5,n,7):
        tags_players = pagina_bs.find_all("td", {"class": "zentriert"})[i]
      # In our case, we are finding all anchors with the class "zentriert"
        for tag_player in tags_players:
          Assists_players.append(tag_player)
    
    Assists_players
    
    """Market Price"""
    
    market_players = []
    
    tags_player = pagina_bs.find_all("td", {"class": "hauptlink rechts"})
    
    for tag_player in tags_player:
        text = tag_player.text
        # The price text contains characters that we don’t need like £ (euros) and m (million) so we’ll remove them
        text_rep = text.replace("£", "").replace("m","0000").replace("Th.","000").replace(".","")
        # We will now convert the value to a numeric variable (float)
        market_players.append(text_rep)
    
    market_players
    
    """  DataFrame"""
    
    df = pd.DataFrame({"Name":name_players, "Age":age_players, "Nationality":nationality_players,
                         "Competition":competition_players,"Team":team_players, "Match":match_players,
                         "Goal":goal_players,"Assists":Assists_players,"Market price":market_players})
    
    return df

def data_csv(year,age,n_page):

  df = extract(year,age,1)
  for i in range(2,n_page):  ## Extract for page
    df= df.append(extract(year,age,i), ignore_index=True)
    
  df[["Age","Match","Goal","Market price"]]=df[["Age","Match","Goal","Market price"]].astype(str).astype(int)
    
  df[["Market price"]]= round((df[["Market price"]]/1000000)*1.15,2)
    
  df.to_csv("Players_under{}.csv".format(age))



if __name__ == '__main__':
  """
  Extract database from transfermarket"
  """

    year=2022
    age=25
    n_page=11

    data_csv(year,age,n_page)
