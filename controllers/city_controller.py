from flask import Flask, Blueprint, render_template, redirect, request 
from models.city import City 
from repositories import city_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_blueprint = Blueprint("city", __name__)

#INDEX 
#GET '/cities'
@city_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

#NEW 
# GET '/cities/new' --> to create a new city 
@city_blueprint.route("/cities/new", methods= ["GET"])
def new_city():
    countries = country_repository.select_all()
    return render_template ("cities/new.html", all_countries=countries)

#CREATE
#POST - '/cities' --> to handle to post from the new 
@city_blueprint.route("/cities", methods= ["POST"])
def create_city():
    #data from form 
    city_name = request.form['city_name']
    date_of_travel = request.form['date_of_travel']
    visited = request.form['visited']

    #select the country using the repository 
    country = country_repository.select(country_id)
    
    #create a new city
    city = City(city_name, date_of_travel, visited)

    #save the city back to the database with the save method
    city_repository.save(city)
    return redirect("/cities")


#SHOW
#GET '/cities/<id>'


#DELETE '/cities/<id>'
@city_blueprint.route("/cities/<id>/delete", methods = ['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")

#? UPDATE OR EDIT