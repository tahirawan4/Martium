# FeedLy
FeedLy

Project Setup:

Install Virtual environment with python3

Go inside the project and install requirements
    
    pip install -r requirements


Setup PostgreSql:

    sudo su - postgres
    psql
    
Commands inside PSQL:
    
    CREATE DATABASE feedly;
    CREATE USER feedly WITH PASSWORD '1234567a';
    GRANT ALL PRIVILEGES ON DATABASE feedly TO feedly;

Running Project:

    First run migrations
    python manage.py migrate # This will create default tables in your databases
    
    Run Project
    python manage.py runserver
    
    You can also specify a settings file using from command line
    
    python manage.py runserver 127.0.0.1:8000 --settings=feedly.settings.local 
    
