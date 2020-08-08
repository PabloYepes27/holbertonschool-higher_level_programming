# 0x0F. Python - Object-relational mapping


## Contents:open_file_folder:

- Project Description:newspaper:
- General Objectives:bulb:
- Instalation:wrench:
- Command Interpreter Description:computer:

	* How to start it
	* Commands and their usage
	* How to use it
	* examples

- Unittests:boom:
- Tasks:clipboard:
- Built with:hammer:
- Resources:books:
- Author:black_nib:

---

## Project Description:newspaper:

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

---

## General Objectives:bulb:

* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

---

## Instalation:wrench:

Follow the following instructions to get a copy of the program and run in your local machine.

* Clone the following repository.
```
https://github.com/PabloYepes27/holbertonschool-higher_level_programming.git
```

* Run the program
```
./file.py
```

---

## Tasks:clipboard:

### [0. My privileges!](./0-privileges.sql)
* Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).


### [1. Root user](./1-create_user.sql)
* Write a script that creates the MySQL server user user_0d_1. 


### [2. Read user](./2-create_read_user.sql)
* Write a script that creates the database hbtn_0d_2 and the user user_0d_2. 


### [3. Always a name](./3-force_name.sql)
* Write a script that creates the table force_name on your MySQL server.


### [4. ID can't be null](./4-never_empty.sql)
* Write a script that creates the table id_not_null on your MySQL server.


### [5. Unique ID](./5-unique_id.sql)
* Write a script that creates the table unique_id on your MySQL server.


### [6. States table](./6-states.sql)
* Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.


### [7. Cities table](./7-cities.sql)
* Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.


### [8. Cities of California](./8-cities_of_california_subquery.sql)
* Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.


### [9. Cities by States](./9-cities_by_state_join.sql)
* Write a script that lists all cities contained in the database hbtn_0d_usa.


### [10. Genre ID by show](./10-genre_id_by_show.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download


### [11. Genre ID for all shows](./11-genre_id_all_shows.sql)
* Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)


### [12. No genre](./12-no_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)


### [13. Number of shows by genre](./13-count_shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)


### [14. My genres](./14-my_genres.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)


### [15. Only Comedy](./15-comedy_only.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)


### [16. List shows and genres](./16-shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)


### [17. Not my genre](./100-not_my_genres.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)


### [18. No Comedy tonight!](./101-not_a_comedy.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 100-not_my_genres.sql)


### [19. Rotten tomatoes](./102-rating_shows.sql)
* Import the database hbtn_0d_tvshows_rate dump to your MySQL server: download


### [20. Best genre](./103-rating_genres.sql)
* Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)

---

## Built with:hammer:

Python
MySQL
MySQLdb
SQLAlchemy
Flask

---

## Resources:books:

* [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
* [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/)
* [MySQLdb tutorial](http://www.mikusa.com/python-mysql-docs/index.html)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient-python)
* [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
* [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
* [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
* [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
* [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

---

## Author:black_nib:

* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)
