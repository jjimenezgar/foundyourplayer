#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:03:35 2022

@author: jjimenez
"""

from symbol import comp_for
import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from matplotlib import offsetbox
import main_db
import utils
# Crear el server Flask
app = Flask(__name__)
db = SQLAlchemy()

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///player_under25.db"

# Asociamos nuestro controlador de la base de datos con la aplicacion

main_db.db.init_app(app)

# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        # Renderizar el temaplate HTML index.html
        print("Renderizar index.html")
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/goal
@app.route("/goal", methods=['GET','POST'])
def goal():

    if request.method == 'GET':
        # Si entré por "GET" es porque acabo de cargar la página
        try:
            # Renderizar el temaplate HTML tabla.html
            data = main_db.top_players(10)

            print("Renderizar tabla.html")
            return render_template('tabla.html', data=data)

        except:
            return jsonify({'trace': traceback.format_exc()})
        #Obtener el reporte
    if request.method == 'POST':
        #access the data from form
        try:
            age = (request.form["age"])
            if not age:
                age=0
            
            nat = (request.form["nationality"])
            
            if not nat:
                nat=0

            comp = (request.form["competition"])
            if not comp:
                comp=0

            price= (request.form["price"])
            if not price:
                price = 0


        #get data
        # Obtener el reporte

            data = main_db.top_players(10,age,nat,comp,price)
        
        # Renderizar el temaplate HTML tabla_filter.html
            print("Renderizar tabla.html")
            return render_template('tabla_filter.html', data=data)
        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/scorers")
def scorers():
            x,y=main_db.scorers()

            image_html = utils.graficar(x, y,"scorers","goals")
            return Response(image_html.getvalue(), mimetype='image/png')

@app.route("/assists")
def assists():
            x,y=main_db.assists()

            image_html = utils.graficar(x, y,"assists","assists")
            return Response(image_html.getvalue(), mimetype='image/png')



if __name__ == '__main__':
    print('Inove@Server start!')
    
    # Lanzar server
    app.run(host="127.0.0.1", port=5000)