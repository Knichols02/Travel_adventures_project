DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
id SERIAL PRIMARY KEY,
name VARCHAR(255)
);

CREATE TABLE cities (
id SERIAL PRIMARY KEY,
city_name VARCHAR (255),
date_of_travel INT,
visited BOOLEAN, 
countries_id INT REFERENCES countries(id)
);