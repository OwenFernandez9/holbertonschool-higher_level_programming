--  lists all cities contained in the database hbtn_0d_usa.
SELECT city_id AS id, city_name AS name, state_name AS name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;