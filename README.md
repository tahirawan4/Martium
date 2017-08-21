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
