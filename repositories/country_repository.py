#CRUD ACTIONS GO HERE  

from db.run_sql import run_sql
from models.country import Country 
from models.city import City
import repositories.country_repository as country_repository

#CREATE/SAVE  
def save(country_to_save):
    sql = "INSERT INTO countries(name) VALUES (%s) RETURNING id"
    values = []
#READ - SELECT ALL 

#READ - SELECT ONE 

#DELETE - DELETE ALL 

#DELETE - DELETE ONE 

#UPDATE (ONE)
