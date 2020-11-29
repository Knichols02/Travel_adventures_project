import pdb
from models.country import Country
from models.city import City 

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()


country1 = Country('Italy')
country_repository.save(country1)

country2 = Country('France')
country_repository.save(country2)

country3 = Country('USA')
country_repository.save(country3)

country4 = Country('Croatia')
country_repository.save(country4)

country5 = Country('Hungary')
country_repository.save(country5)

pdb.set_trace()
