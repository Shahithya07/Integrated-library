# Integrated library
Software created using python,mysql

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project keeps track about the books in the library.
	
## Technologies
Project is created with:
* python version: 3.9.13
* mysql: 8.0.25
	
## Setup
To run this project, install it locally using cmd:

```
pip install tkinter
pip install pymysql
```
## Description of tables in database
Create three tables in the database
* books
* books_issued
* student

create database db;

create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));

create table books_issued(bid varchar(20) primary key, name varchar(30), issuedDate date, returnDate date);

create table student(register_number int, name varchar(50), emailId varchar(60), PhoneNumber varchar(10), password varchar(100));


