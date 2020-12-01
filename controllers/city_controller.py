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
    return render_template("cities/index.html", cities = cities)

#NEW 
# GET '/cities/new' --> to create a new city 
@city_blueprint.route("/cities/new", methods= ["GET"])
def new_city():
    countries=country_repository.select_all()
    return render_template ("cities/new.html", countries=countries)

# #NEW 
# #GET '/cities/future'
@city_blueprint.route("/cities/future", methods= ["GET"])
def future_trip():
    cities = city_repository.select_all()
    return render_template("/cities/future.html", cities = cities)

#CREATE
#POST - '/cities' --> to handle to post from the new 
@city_blueprint.route("/cities", methods= ["POST"])
def create_city():
    #data from form 
    city_name = request.form['city_name']
    date_of_travel = request.form['date_of_travel']
    visited = request.form['visited']

    #select the country using the repository 
    country = country_repository.select(request.form['country'])
    
    #create a new city
    city = City(city_name, date_of_travel, visited)

    #save the city back to the database with the save method
    city_repository.save(city)
    if city.visited:
        return redirect("/cities")
    else:
        return redirect("/cities/future")



#SHOW
#GET '/cities/<id>'
@city_blueprint.route("/cities/<id>", methods=["GET"])
def show_city(id):
    city = city_repository.select(id)
    return render_template("/cities/show.html", city = city)

#DELETE '/cities/<id>'
@city_blueprint.route("/cities/<id>/delete", methods = ['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")

#EDIT 
#GET '/cities<id>/edit'
@city_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", city=city, countries = countries)

# UPDATE
# PUT '/cities/<id>'
@city_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    city_name = request.form["city_name"]
    date_of_travel = request.form["date_of_travel"]
    visited = request.form["visited"]
    city = City(city_name, date_of_travel, visited, id)
    city_repository.update(city)
    return redirect("/cities")
