# Indicator Library

## Background

The Indicator Library originated as an initiative to gather and organize approximately 2,500 frequently utilized indicators employed by NGOs and donors in the international development and humanitarian sector. This also encompasses indicators utilized in corporate reporting on the Sustainable Development Goals (SDGs).

The primary objective of the project is to enhance the utilization of indicators. It aims to achieve this by advocating for standard, reusable indicators and providing guidance to assist users in efficiently planning and collecting valuable data for their projects.

## Interested in contributing?

Create an issue and we'll get in touch.

## Install

Here are the steps to create tables in PostgreSQL
1. Set up Postgres
      * Refer to this document https://docs.djangoproject.com/en/1.7/intro/tutorial01/ , chapter Database Setup
      Create git clone of indicator- library locally - git clone https://github.com/toladata-foundation/indicator-library
     
      * (For Windows users, download python for windows 3.6.4 (IDLE, PIP) python-3.6.4.exe and install it)
      * Confirm python --version (3.6.4)
     
2. Run Django Application:

      python manage.py runserver
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
            
## For dev team
* run scripts/Csvtomodel.py file with the clean dataset provided in the django shell(python manage.py shell)
