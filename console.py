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

country7 = Country('England')
country_repository.save(country7)

country8 = Country('Costa Rica')
country_repository.save(country8)


city1 = City('Rome', country1, 2014, True)
city_repository.save(city1)

city2 = City('Paris', country2, 2014, True)
city_repository.save(city2)

city3 = City('Washington D.C.', country3, 2016, True)
city_repository.save(city3)

city4 = City('Dubrovnik', country4, 2015, True)
city_repository.save(city4)

city5 = City('Budapest', country5, 2014, True)
city_repository.save(city5)


pdb.set_trace()
