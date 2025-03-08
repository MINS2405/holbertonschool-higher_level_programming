-- Create the table id_not_null in the specified database.
-- This script creates the table id_not_null with an id column that cannot be NULL and has a default value of 1.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
