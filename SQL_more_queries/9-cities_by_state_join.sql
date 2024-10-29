--  lists all cities contained in the database hbtn_0d_usa.
SELECT city_id AS id, city_name AS name, state_name AS name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California' OR name = 'Arizona')
ORDER BY city_id ASC;