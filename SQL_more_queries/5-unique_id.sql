-- Create the table unique_id in the specified database.
-- This script creates the table unique_id with an id column that has a default value of 1 and must be unique.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
