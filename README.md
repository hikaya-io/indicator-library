# Indicator Library

## Background

TolaData is supporting an open source project called the Indicator Library, which started as an exercise to collect and compile nearly 2,500 commonly used indicators used by NGOs and donors in the international development and humanitarian sector as well as to include indicators used for corporate reporting on the SDGs. 

The project’s goal is to improve the use of indicators by promoting standard, reusable indicators alongside guidance to help users effectively plan and collect useful data for their projects.

## Interested in contributing?

See our tasks list: https://github.com/toladata-ce/indicator-library/projects/1

## Install

Here are the steps to create tables in PostgreSQL
1. Set up Postgres
      * Refer to this document https://docs.djangoproject.com/en/1.7/intro/tutorial01/ , chapter Database Setup
      Create git clone of indicator- library locally - git clone https://github.com/toladata-foundation/indicator-library
     
      * (For Windows users, download python for windows 3.6.4 (IDLE, PIP) python-3.6.4.exe and install it)
      * Confirm python --version (3.6.4)
     
2. Run Django Application:
      * Install django with ͞pip install django͟. 
      * Verify version 2.0.2 with django-admin –version
      * pip install psycopg2  (2.7.4)
      * pip3 install djangorestframework
      * python manage.py runserver
      
3. psql -U postgres with your password -create user and password; 
      * create database indicator_library 
      * grant all privileges on database indicator_library to indlib 
      * python manage.py migrate
      * Psql with indlib account, it creates the following tables: 
            auth_group      
            auth_group_permissions    
            auth_permission            
            auth_user             
            auth_user_groups           
            auth_user_user_permissions 
            django_admin_log           
            django_content_type             
            django_migrations  
            django_session     
