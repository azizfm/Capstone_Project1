import os
import pymysql
from forms import AddForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################ 

# SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mutahabe@localhost/capstone1_schema'  # + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class sales_records(db.Model):   # sqlAlchemy Model = Table & Table object
    __tablename__ = 'sales_records'
    prod_id = db.Column(db.Text, primary_key=True)
    emp_id = db.Column(db.Text)
    prod_qty = db.Column(db.Integer)
    date = db.Column(db.Date)

    '''
    prod_id = StringField('Product Name :')            ####  Name of Puppy:
    emp_id = StringField('Employee ID')  ####   Name of Owner
    prod_qty = IntegerField("Product Quantity: ")
    date = DateField("Date")
  
    '''

    def __init__(self, prod_id, emp_id):
        self.prod_id = prod_id
        self.emp_id = emp_id


db.create_all()


############################################

# VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
                                                     ## 1  grabbing the data from web page
        prod_id = form.prod_id.data
        emp_id = form.emp_id.data
        prod_qty = form.prod_qty.data
        date = form.date.data

                                                     ## 2 assigning to sales object
        new_sales = sales_records(prod_id, emp_id)
        new_sales.prod_qty = prod_qty
        new_sales.date = date
        print(new_sales)

                                             # 3 adding the sales object to MySQL database (update part of CRUD)
        db.session.add(new_sales)
        db.session.commit()

        '''   name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        '''
        return redirect(url_for('add_pup'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
