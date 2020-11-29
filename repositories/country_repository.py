#CRUD ACTIONS GO HERE  

from db.run_sql import run_sql
from models.country import Country 
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

#CREATE/SAVE  
def save(country):
    sql = "INSERT INTO countries(name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0] ['id']
    country.id = id
    return country 

#READ - SELECT ALL 

#READ - SELECT ONE 

#DELETE - DELETE ALL 
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

#DELETE - DELETE ONE 
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE (ONE)
def update(country):
    sql = "UPDATE countries SET (name) = (%s) WHERE id = %s"
    values = [country.name]
    run_sql(sql, values)