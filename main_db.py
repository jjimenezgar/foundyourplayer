#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:03:35 2022

@author: jjimenez
"""

import os
import csv
import sqlite3
import pandas as pd
from sqlalchemy import func
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()

############ Create DB ########

from config import config

# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
dataset = config('dataset', config_path_name)

### crear una clase de la tabla y sus columnas
class Players(db.Model):
    __tablename__ = "players"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    age= db.Column(Integer)
    nationality=db.Column(String)
    competition=db.Column(String)
    team=db.Column(String)
    match= db.Column(Integer)
    goal= db.Column(Integer)
    assists=db.Column(Integer)
    price= db.Column(Integer)

    
    def __repr__(self):
        return f"Player:{self.name} is from {self.nationality}"
    
   
def insert_persona(name, age, nationality,competition,team,match,goal,assists,price):
  
    # Buscar por nacionalidad
    query = db.session.query(Players).filter(Players.nationality == nationality)
    country = query.first()

    if nationality is None:
        # Podrá ver en este ejemplo que sucederá este error con la persona
        print(f"Error to create player {name}, doesn't exist the nationality {country}")
        return

    # Crear la persona
    person = Players(name=name, age=age, nationality=nationality,competition=competition,team=team,match=match,goal=goal,assists=assists,price=price)

    # Agregar la persona a la DB
    db.session.add(person)
    db.session.commit()
    print(person)
    
def fill():
    # Insertar el archivo CSV de personas
    # Insertar todas las filas juntas
    with open(dataset["player"]) as fi:
        data = list(csv.DictReader(fi))

        for row in data:
            insert_persona(row['Name'],(row['Age']), row['Nationality'],row['Competition'],row['Team'],(row['Match']),(row['Goal']),(row['Assists']),(row['Market price']))


            
def show(limit=0):


    # Buscar todas las personas
    query = db.session.query(Players).order_by(Players.goal.desc())

    # Si está definido el limite aplicarlo
    if limit > 0:
        query = query.limit(limit)

    # Leer una persona a la vez e imprimir en pantalla
    for player in query:
        print(player)
 
        
def count_player(nationality):
    
    result = db.session.query(Players).filter(Players.nationality == nationality).count()
    print('Players from', nationality, 'found:', result)
    
def top_players(limit,age=0,nationality=0,competition=0,price=0):
    """
    Esta función permite filtrar la tabla con las estadisticas de los jugadores
    """
    json_result_list =[]
    query = db.session.query(Players.name,Players.age,Players.nationality,Players.team,Players.competition,Players.match,Players.goal,Players.assists,Players.price).order_by(Players.goal.desc())

    if age == 0:
        query=query.filter(Players.age != 0)
    else:
        query=query.filter(Players.age < age)

    if nationality == 0:
        query=query.filter(Players.nationality != 0)
    else:
        query=query.filter(Players.nationality == nationality)
   
    if competition == 0:
        query=query.filter(Players.competition != 0)
    else:
        query=query.filter(Players.competition == competition)

    if price == 0:
        query=query.filter(Players.price != 0)
    else:
        query=query.filter(Players.price < price)


    query= query.limit(limit).all()

    for result in query:
        player = result[0]
        age = result[1]
        nationality = result[2]
        team= result[3]
        competition= result[4]
        match=result[5]
        goal = result[6]
        assists=result[7]
        price=result[8]
        json_result = {}
        json_result['name'] = player
        json_result['age'] = age
        json_result['nationality'] = nationality
        json_result['team']=team
        json_result['competition'] = competition
        json_result['match']=match
        json_result['goal'] = goal
        json_result['assists'] = assists
        json_result['price'] = price
        json_result_list.append(json_result)

    return json_result_list

def scorers():

    """
    Obtenemos el top 10 de goleadores

    """

    goal_country = db.session.query(Players.name,Players.goal).order_by(Players.goal.desc()).limit(10).all()

    name_list=[]
    goals_list=[]
    for result in goal_country:
        name=result[0]
        name_list.append(name)
        goals=result[1]
        goals_list.append(goals)

    return name_list, goals_list

def assists():

    """
    Obtenemos el top 10 de asistentes
    """

    goal_country = db.session.query(Players.name,Players.assists).order_by(Players.assists.desc()).limit(10).all()

    name_list=[]
    assists_list=[]
    for result in goal_country:
        name=result[0]
        name_list.append(name)
        assists=result[1]
        assists_list.append(assists)

    return name_list, assists_list


def goal_country():
    """
    Nacionalidades con mas goles
    """

    goal_country = db.session.query(Players.nationality,func.sum(Players.goal)).group_by(Players.nationality).order_by(func.sum(Players.goal).desc()).limit(10).all()

    country_list=[]
    goals_list=[]
    for result in goal_country:
        country=result[0]
        country_list.append(country)
        goals=result[1]
        goals_list.append(goals)

    print(country_list)


    return country_list, goals_list


    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Crear una aplicación Flask para testing
    # y una base de datos fantasma (auxiliar o dummy)
    # Referencia:
    # https://stackoverflow.com/questions/17791571/how-can-i-test-a-flask-application-which-uses-sqlalchemy
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///player_under25.db"
    # Bindear la DB con nuestra app Flask

    
    db.init_app(app)
    app.app_context().push()
    #db.session.remove()
    #db.drop_all()
    #db.create_all()
    # Insertar nacionalidades y personas
    #fill()
    show()
    
