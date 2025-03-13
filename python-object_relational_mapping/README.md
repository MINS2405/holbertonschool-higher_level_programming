# holbertonschool-higher_level_programming - python-object_relational_mapping

**Project Badge:** 63.82%

**By: Guillaume (Adapted by Javier Valenzani)**

## Description

This project explores Object-Relational Mapping (ORM) to connect Python with MySQL databases. You'll use `MySQLdb` for direct SQL queries and `SQLAlchemy` for ORM, abstracting database interactions to Python objects.

## Learning Objectives

*   Connect to a MySQL database from Python.
*   SELECT, INSERT rows in MySQL using Python.
*   Understand ORM concepts.
*   Map Python Classes to MySQL tables.

## Requirements

*   Ubuntu 20.04 LTS, Python 3.8.5
*   `MySQLdb` version 2.0.x
*   `SQLAlchemy` version 1.4.x
*   pycodestyle (version 2.7.*)
*   All files must be executable.
*   All modules, classes, and functions must have documentation.

## Setup

1.  Install MySQL 8.0 on Ubuntu 20.04 LTS:
    ```
    sudo apt update
    sudo apt install mysql-server
    mysql --version
    ```
2.  Connect to MySQL:
    ```
    sudo mysql
    ```
3.  Install MySQLdb:
    ```
    sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
    sudo pip3 install mysqlclient
    python3
    import MySQLdb
    MySQLdb.version_info
    ```
4.  Install SQLAlchemy:
    ```
    sudo pip3 install SQLAlchemy
    python3
    import sqlalchemy
    sqlalchemy.__version__
    ```

## Tasks

### 0. Get all states

Write a script to list all states from the `hbtn_0e_0_usa` database.

*   Takes 3 arguments: mysql username, mysql password, database name.
*   Uses `MySQLdb` to connect to the MySQL server (localhost:3306).
*   Results sorted in ascending order by `states.id`.

### 1. Filter states

Write a script to list all states with a name starting with 'N' from the `hbtn_0e_0_usa` database.

*   Takes 3 arguments: mysql username, mysql password, database name.
*   Uses `MySQLdb`.
*   Results sorted in ascending order by `states.id`.

### 2. Filter states by user input

List values in the `states` table where `name` matches a given argument.

*   Takes 4 arguments: mysql username, mysql password, database name, state name searched.
*   Uses `MySQLdb`.
*   Connects to MySQL server running on localhost at port 3306.

### 3. SQL Injection...

Write a script that's safe from MySQL injections! (Same as Task 2 but secure).

*   Takes 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
*   Uses `MySQLdb`.

### 4. Cities by states

List all cities from the database `hbtn_0e_4_usa`.

*   Takes 3 arguments: mysql username, mysql password and database name.
*   Uses `MySQLdb`.
*   Connects to a MySQL server running on localhost at port 3306
*   Results must be sorted in ascending order by cities.id

### 5. All cities by state

Lists all cities of that state.

* Takes 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
* Uses `MySQLdb`.

## Installation

1.  Clone the repository:

    ```
    git clone <repository_url>
    ```
2.  Navigate to the project directory:

    ```
    cd <project_directory>
    ```
3.  Install the necessary requirements:

    ```
    pip install -r requirements.txt
    ```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
