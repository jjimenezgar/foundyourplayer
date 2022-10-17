# Foundyourplayer

Este repositorio contiene un proyecto donde se desarrolla una web en la que se puede hacer búsqueda de jugadores jóvenes de las mejores competiciones de fútbol del mundo. :soccer:. El objetivo principal de este proyecto es poner en practica lo aprendido en el curso "Desarrollador Python" de [Inove](https://inove.com.ar/).

[Link repositorio] (https://github.com/jjimenezgar/foundyourplayer)



______________________________________________________________________________________________________________________________________


1- En el archivo ["extract.py"](https://github.com/jjimenezgar/foundyourplayer/blob/master/extract.py) se ponen en uso herramientas de web scraping como **Beautiful Soup** para extraer los datos de la pagina [Transfermarkt](https://www.transfermarkt.co.uk/scorer/topscorer/statistik/2020/plus/3/galerie/0).

2- En el archivo ["main_db.py"](https://github.com/jjimenezgar/foundyourplayer/blob/master/main_db.py) se crea la base de datos que luego utilizamos para nuestra web, usamos **SQLALCHEMY** para realizar las querys. Se pudo utilizar una API para alimentar nuestra pagina web, pero para los propositos de aprendizaje se realizo web scraping.

3- En el archivo ["utils.py"](https://github.com/jjimenezgar/foundyourplayer/blob/master/utils.py) se creo una función que permite **graficar los principales datos en nuestra pagina web**.

4- En el archivo ["app.py"](https://github.com/jjimenezgar/foundyourplayer/blob/master/app.py) **asociamos nuestro controlador de la base de datos con la aplicacion.**
