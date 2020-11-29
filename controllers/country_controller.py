from flask import Flask, Blueprint, render_template, redirect, request 
from models.country import Country 
from repositories import country_repository
import repositories.country_repository as country_repository

country_blueprint = Blueprint("country", __name__)

#INDEX 
#GET '/countries'

#NEW 
# GET '/countries/new'

#CREATE
#POST - '/countries'

#form data 
#select country 
#create a new city
#save the city to the database(with save method)


#SHOW
#GET '/countries/<id>'


#DELETE '/countries/<id>'


#? UPDATE OR EDIT