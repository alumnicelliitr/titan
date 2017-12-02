# Titan

Django project for maintaining apis and central database for the website

## Setup Instructions

- Clone the project locally and cd to the project root
- Make virtual environment using `virtualenv env`
- Activate the virtual environment using `source env/bin/activate`
- Install python dependencies using `pip install -r requirements.txt`
- Setup postgres db locally
- Make a new file `.env` in the root directory with db credentials as per the `sample.env` file
- Run `python manage.py migrate`
