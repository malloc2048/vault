# Vault
Basically a front end on a database (well some data files for now) to hold all the stuff I have around.

Built using Flask and Bootstrap.

# Running Vault
## Dependencies
In order to run this thing you will need the following dependencies: 
* Python 3.10+
* Python Poetry

## Starting Vault:
* activate the poetry shell ``` poetry shell ```
* install all needed dependencies ``` poetry install ```
* run the gunicorn server ```  gunicorn -c vault/config/gunicorn.conf.py vault:app ```
* access from ``` [ip]:8001 ```

## Updating
In order to update Vault simply modify the data files found in ``` vaul/models/data_files ```.  
Specifically the categories.json file holds the supported categories and fields used for the data models  
any jsonl file found contains the data that Vault will display.

## TODO/Future enhancements
* Add button is not working properly
* Get the Search functionality to work
* functionality to deleting entries
* Switch to a database (sqlite) instead of flat jsonl files
* Move python project management to UV
* Redesign the pages maybe use Tailwinds? 
* Add an auth?
* Maybe consider converting to Golang, or maybe a Django app

## auth reference
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
