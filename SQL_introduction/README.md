# SQL - Introduction

This project is part of the SQL - Introduction course at Holberton School. It covers basic concepts of databases and SQL, including data definition language (DDL), data manipulation language (DML), and basic queries.

## Objectives

- Understand what a database is and how it differs from a relational database.
- Learn what SQL stands for and how to use it.
- Understand how to create a database in MySQL.
- Learn about DDL and DML statements.
- Understand how to create or alter tables.
- Learn how to select data from tables.
- Understand how to insert, update, or delete data.
- Learn about subqueries and MySQL functions.

## Tasks

1. **List databases** : Write a script that lists all databases of your MySQL server.
2. **Create a database** : Write a script that creates the database `hbtn_0c_0` in your MySQL server.
3. **Delete a database** : Write a script that deletes the database `hbtn_0c_0` from your MySQL server.
4. **List tables** : Write a script that lists all tables of a database in your MySQL server.
5. **First table** : Write a script that creates a table called `first_table` in the current database.
6. **Full description** : Write a script that prints the description of the table `first_table`.
7. **List all in table** : Write a script that lists all rows of the table `first_table`.
8. **First add** : Write a script that inserts a new row into the table `first_table`.
9. **Count 89** : Write a script that displays the number of records with `id = 89` in the table `first_table`.
10. **Full creation** : Write a script that creates a table called `second_table` and adds multiple rows.
11. **List by best** : Write a script that lists all records of the table `second_table`, ordered by score.
12. **Select the best** : Write a script that lists all records with a score >= 10 in the table `second_table`.
13. **Cheating is bad** : Write a script that updates the score of "Bob" to 10 in the table `second_table`.
14. **Score too low** : Write a script that removes all records with a score <= 5 in the table `second_table`.
15. **Average** : Write a script that computes the average score of all records in the table `second_table`.
16. **Number by score** : Write a script that lists the number of records with the same score in the table `second_table`.
17. **Say my name** : Write a script that lists all records of the table `second_table`, excluding rows where the name is empty.

## Execution

To run the SQL scripts, ensure you have MySQL 8.0 installed on your system. Use the command `mysql` to execute each SQL file.

## Authors

- https://github.com/MINS2405/holbertonschool-higher_level_programming/

## License

This project is under the MIT License.

import requests

def get_readme_content(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/readme"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        readme_url = data['download_url']
        readme_response = requests.get(readme_url)
        return readme_response.text
    else:
        return None




