from starter_code_section_5.app import app
from starter_code_section_5.db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
