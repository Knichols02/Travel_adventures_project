from flask import Flask, Blueprint, render_template, redirect, request 
from models.country import Country 
from repositories import country_repository
import repositories.country_repository as country_repository

country_blueprint = Blueprint("country", __name__)

#INDEX 
#GET '/countries'
@country_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

#NEW 
# GET '/countries/new' --> show html form to create a new task

#CREATE
#POST - '/countries'

#form data 
#select country 
#create a new city
#save the city to the database(with save method)


#SHOW
#GET '/countries/<id>'


#DELETE '/countries/<id>'
@country_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')

#? UPDATE OR EDIT