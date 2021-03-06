#CRUD ACTIONS GO HERE  

from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

#CREATE/SAVE  
def save(city):
    sql = "INSERT INTO cities (city_name, country_id, date_of_travel, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [city.city_name, city.country.id, city.date_of_travel, city.visited]
    results = run_sql(sql, values)
    #import pdb; pdb.set_trace()
    id = results[0]['id']
    city.id = id
    return city 

#READ - SELECT ALL 
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['date_of_travel'], row['visited'], row['id'])
        cities.append(city)
    return cities

#READ - SELECT ONE 
def select(id):
    city = None 
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values) [0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['city_name'], result['date_of_travel'], result['visited'], country, result['id'])
    return city 

#DELETE - DELETE ALL 
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

#DELETE - DELETE ONE 
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE (ONE)
def update(city):
    sql = "UPDATE cities SET (city_name, date_of_travel, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.city_name, city.date_of_travel, city.visited]
    run_sql(sql, values)


def select_all_unvisited():
    sql = "SELECT * FROM cities WHERE visited = 'f'"
    results = run_sql(sql)
    cities =[]

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['date_of_travel'], row['visited'], row['id'])
        cities.append(city)
    return cities
