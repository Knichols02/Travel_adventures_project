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

country6 = Country('Australia')
country_repository.save(country6)


city1 = City('Rome', 2014, True)
city_repository.save(city1)

city2 = City('Paris', 2014, True)
city_repository.save(city2)

city3 = City('Washington D.C.', 2016, True)
city_repository.save(city3)

city4 = City('Dubrovnik', 2015, True)
city_repository.save(city4)

city5 = City('Budapest', 2014, True)
city_repository.save(city5)

city6 = City('Sydney', 0000, False)
city_repository.save(city6)

pdb.set_trace()
