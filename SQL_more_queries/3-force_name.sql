-- Create the table force_name in the specified database.
-- This script creates the table force_name with an id and a name column.
-- The name column is required (NOT NULL).

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
