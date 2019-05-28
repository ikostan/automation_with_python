"""

BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically and makes sure that it is a new,
blank database each time.

"""


import unittest
from starter_code.app import app
from starter_code.db import db


class BaseTest(unittest.TestCase):

    def setUp(self):

        #  runs before each test
        #  make sure database exists
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'

        #  instantiate test app client and create DB
        with app.app_context():
            db.init_app(app)
            db.create_all()

        #  get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        #  runs after each test
        #  make sure that DB is blank
        with app.app_context():
            db.session.remove()  # clean the session
            db.drop_all()  # delete everything from db

