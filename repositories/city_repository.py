#CRUD ACTIONS GO HERE  

from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository


#CREATE/SAVE  
def save(city):
    sql = "INSERT INTO cities (city_name, date_of_travel, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [city.city_name.id, city.date_of_travel.id, city.visited.id]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city 

#READ - SELECT ALL 
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City

#READ - SELECT ONE 

#DELETE - DELETE ALL 

#DELETE - DELETE ONE 

#UPDATE (ONE)