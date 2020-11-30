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
@country_blueprint.route("/countries/new")
def new_country():
    return render_template("/countries/new.html")

#CREATE
#POST - '/countries'
@country_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    country = Country(name)
    country_repository.save(country)
    return redirect("/countries")

#SHOW
#GET '/countries/<id>'

#DELETE '/countries/<id>'
@country_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')

#EDIT
#GET '/cities<id>/edit'
@country_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country=country)

#UPDATE "/countries/<id>"
@country_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    country = Country(name, id)
    country_repository.update(country)
    return redirect("/countries")