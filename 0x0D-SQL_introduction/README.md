# 0x0D. SQL - Introduction

<gif  width="520"  alt="image"  src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg">

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

This is the first project of SQL, in this project you going to see what is a relational database, how to create and modify them.

---

## General Objectives:bulb:

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

---

## Instalation:wrench:

Follow the following instructions to get a copy of the program and run in your local machine.

* Clone the following repository.
```
https://github.com/PabloYepes27/holbertonschool-higher_level_programming.git
```


* Run the program
```
cat file.sql | mysql -hlocalhost -uroot -p
```

---

## Tasks:clipboard:

### [0. List databases](./0-list_databases.sql)
* Write a script that lists all databases of your MySQL server.


### [1. Create a database](./1-create_database_if_missing.sql)
* Write a script that creates the database hbtn_0c_0 in your MySQL server.


### [2. Delete a database](./2-remove_database.sql)
* Write a script that deletes the database hbtn_0c_0 in your MySQL server.


### [3. List tables](./3-list_tables.sql)
* Write a script that lists all the tables of a database in your MySQL server.


### [4. First table](./4-first_table.sql)
* Write a script that creates a table called first_table in the current database in your MySQL server.


### [5. Full description](./5-full_table.sql)
* Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.


### [6. List all in table](./6-list_values.sql)
* Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.


### [7. First add](./7-insert_value.sql)
* Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.


### [8. Count 89](./8-count_89.sql)
* Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.


### [9. Full creation](./9-full_creation.sql)
* Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.


### [10. List by best](./10-top_score.sql)
* Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.


### [11. Select the best](./11-best_score.sql)
* Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.


### [12. Cheating is bad](./12-no_cheating.sql)
* Write a script that updates the score of Bob to 10 in the table second_table.


### [13. Score too low](./13-change_class.sql)
* Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.


### [14. Average](./14-average.sql)
* Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.


### [15. Number by score](./15-groups.sql)
* Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.


### [16. Say my name](./16-no_link.sql)
* Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.


### [17. Go to UTF8](./100-move_to_utf8.sql)
* Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.


### [18. Temperatures #0](./101-avg_temperatures.sql)
* Import in hbtn_0c_0 database this table dump: download


### [19. Temperatures #1](./102-top_city.sql)
* Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)


### [20. Temperatures #2](./103-max_state.sql)
* Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

---

## Built with:hammer:

MySQL

---

## Resources:books:

Read or watch:
* [Concept page Databases](https://intranet.hbtn.io/concepts/37)
* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
* [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
* [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)
* [Introduction to SQL - Socrática](https://www.youtube.com/playlist?list=PLi01XoE8jYojRqM4qGBF1U90Ee1Ecb5tt)
* [Intro to SQL basics - Khanacademy](https://www.khanacademy.org/computing/computer-programming/sql/sql-basics/pt/aggregating-data)
* [How to Create a Database from a Script in MySQL](https://database.guide/how-to-create-a-database-from-a-script-in-mysql/)
* [SQL syntax check validator](https://www.eversql.com/sql-syntax-check-validator/)

---

## Author:black_nib:

* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)
