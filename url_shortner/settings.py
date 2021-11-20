import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')