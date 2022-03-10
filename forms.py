from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField



class AddForm(FlaskForm):

    prod_id = StringField('Product ID :')            ####  Name of Puppy:
    emp_id = StringField('Employee ID')  ####   Name of Owner
    prod_qty = IntegerField("Product Quantity: ")
    date = DateField("Date")
    submit = SubmitField('SUBMIT')
