class City:
    def __init__(self, city_name, country, date_of_travel, visited= False, id= None):
        self.city_name = city_name 
        self.date_of_travel = date_of_travel
        self.visited = visited
        self.country = country
        self.id = id
    