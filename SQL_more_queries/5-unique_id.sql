-- create a table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL UNIQUE DEFAULT 1,
	NAME varchar(256)
);
