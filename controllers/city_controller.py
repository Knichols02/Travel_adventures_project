from flask import Flask, Blueprint, render_template, redirect, request 
from models.city import City 
from repositories import city_repository
import repositories.city_repository as city_repository

city_blueprint = Blueprint("city", __name__)

#INDEX 
#GET '/cities'
@city_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

#NEW 
# GET '/cities/new'

#CREATE
#POST - '/cities'

#form data 
#select country 
#create a new city
#save the city to the database(with save method)


#SHOW
#GET '/cities/<id>'


#DELETE '/cities/<id>'
@city_blueprint.route("/cities/<id>")
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")

#? UPDATE OR EDIT