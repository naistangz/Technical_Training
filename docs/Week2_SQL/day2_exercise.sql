-- drop database
DROP DATABASE anais_db

-- create database
CREATE DATABASE anais_db

-- using a database
USE anais_db

DROP TABLE anais_films

-- creating a table 
CREATE TABLE anais_films
(
    film_id INT IDENTITY(1,1) PRIMARY KEY,
    film_name VARCHAR(10) NOT NULL,
    film_type VARCHAR(50)
)

-- alter table 
-- ALTER TABLE anais_films
-- ADD film_id INT IDENTITY

INSERT INTO anais_films VALUES
(
('Star Wars', 'Sci fi'),
('Star Trek', 'Sci fi')
)

INSERT INTO anais_films VALUES
('Batman', 'Action')

-- INSERT INTO anais_films(
--     film_name, film_type, release_date, director, writer, star, film_language, official_website, plot_summary
-- )
-- VALUES(
--     'SQL', 'Romance', '2000-02-20', 'Neil Armstrong', 'Anais', 4.5, 'japanese', 'www.sql.com', 'a very painful journey into DevOps'
-- );

SELECT * FROM anais_films;

DROP TABLE director 

CREATE TABLE director(
    director_id INT,
    director_name VARCHAR(50),
    city VARCHAR(20) DEFAULT 'LONDON',
    film_id INT,
    PRIMARY KEY(director_id),
    FOREIGN KEY(film_id) REFERENCES anais_films(film_id)

)

ALTER TABLE anais_films
ADD film_id INT IDENTITY PRIMARY KEY


INSERT INTO director
(director_name, film_id)
VALUES 
('Steve', 1),
('Tom', 2)

INSERT INTO director
(director_name, film_id)
VALUES
('Bob', 4)

SELECT * FROM director
SELECT * FROM anais_films;

/*Why is this not working Auto and manual way*/
DELETE FROM anais_films WHERE film_id =1

UPDATE director SET director= 'Jamie' where film_id = 1