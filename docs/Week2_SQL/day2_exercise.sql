-- DELETING DATABASE
DROP DATABASE anais_db

-- CREATING DATABASE
CREATE DATABASE anais_db

-- USING A DATABASE
USE anais_db

DROP TABLE film_table

-- CREATING THE FIRST TABLE
CREATE TABLE film_table
(
    film_name VARCHAR(15),
    film_type VARCHAR(15),
    release_date DATETIME,
    director CHAR(15),
    writer CHAR(15),
    Star DECIMAL(2, 1),
    film_language CHAR(15),
    official_website VARCHAR(40),
    plot_summary VARCHAR(MAX)
)

-- ALTERING THE TABLE
ALTER TABLE film_table ADD film_id INT IDENTITY PRIMARY KEY;

INSERT INTO film_table(
    film_name, film_type, release_date, director, writer, star, film_language, official_website, plot_summary
)
VALUES
(
    'SQL', 'Romance', '2000-02-20', 'Neil Armstrong', 'Anais', 4.5, 'japanese', 'www.sql.com', 'a very painful journey into DevOps'
),
(
    'SQL', 'Romance', '2000-02-20', 'Neil Armstrong', 'Anais', 4.5, 'japanese', 'www.sql.com', 'a very painful journey into DevOps'
),
(
    'SQL', 'Romance', '2000-02-20', 'Neil Armstrong', 'Anais', 4.5, 'japanese', 'www.sql.com', 'a very painful journey into DevOps'
);


SELECT * FROM film_table;

-- CREATING A SECOND TABLE
DROP TABLE director;

CREATE TABLE director(
    director_id INT IDENTITY,
    director_name VARCHAR(50),
    city VARCHAR(20) DEFAULT 'LONDON',
    film_id INT,
    PRIMARY KEY(director_id),
    FOREIGN KEY(film_id) REFERENCES film_table(film_id)

)

INSERT INTO director
(director_name, film_id)
VALUES 
('Steve', 1),
('Bob', 2),
('Stacy', 3)


SELECT * FROM director;

-- DELETE FROM film_table WHERE film_id =1
/*Why is this not working Auto and manual way??*/

-- ALTER TABLE director
-- ADD CONSTRAINT film_id
-- FOREIGN KEY (film_id) 
-- REFERENCES film_table (film_id) ON DELETE CASCADE



-- UPDATE director SET director= 'Jamie' where film_id = 2
