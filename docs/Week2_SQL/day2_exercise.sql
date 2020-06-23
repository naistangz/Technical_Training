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
    film_name VARCHAR(15),
    film_type VARCHAR(15),
    date_of_release DATETIME,
    director CHAR(15),
    writer CHAR(15),
    Star DECIMAL(2, 1),
    film_language CHAR(15),
    official_website VARCHAR(40),
    plot_summary VARCHAR(MAX)
)

--alter table 
ALTER TABLE anais_films
ADD release_date DATETIME;

INSERT INTO anais_films(
    film_name, film_type, release_date, director, writer, star, film_language, official_website, plot_summary
)
VALUES(
    'SQL', 'Romance', '2000-02-20', 'Neil Armstrong', 'Anais', 4.5, 'japanese', 'www.sql.com', 'a very painful journey into DevOps'
);

--SP_HELP anais_films;

SELECT * FROM anais_films;

ALTER TABLE anais_films
ADD film_id INT IDENTITY PRIMARY KEY;

DROP TABLE director;

CREATE TABLE director(
    director_id INT IDENTITY,
    director_name VARCHAR(50),
    city VARCHAR(20) DEFAULT 'LONDON',
    film_id INT,
    PRIMARY KEY(director_id),
    FOREIGN KEY(film_id) REFERENCES anais_films(film_id)

)

SELECT * FROM director;

INSERT INTO director
(director_name, film_id)
VALUES 
('Steve', 1),
('Tom', 2)

INSERT INTO director
(director_name, film_id)
VALUES
('Bob', 4)

SELECT * FROM director;


/*Why is this not working Auto and manual way*/

DELETE FROM anais_films WHERE film_id =1

UPDATE director SET director= 'Jamie' where film_id = 1