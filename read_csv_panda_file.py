import pandas as pd
from sqlalchemy import create_engine

my_engine = create_engine('mysql+pymysql://root:mutahabe@localhost/puppies') # creating connection to my_sql database

dog_csv = pd.read_csv('C:\\Users\\azizs\\TEKsystems\\pythonProject\\Dogs_Table.csv')
owner_csv = pd.read_csv("Owners_Table.csv")

print(dog_csv.head())
print(owner_csv.head())

#dog_csv.to_sql(name='puppies', con=my_engine,
#               if_exists='append', index=False)

#owner_csv.to_sql(name='owners', con=my_engine,
#                 if_exists='append', index=False)

dog_df = pd.read_sql('select * from puppies', my_engine)
owner_df = pd.read_sql('select * from owners', my_engine)

print(dog_df.head())
print(owner_df.head())

print(dog_df.shape)   # There are 11 rows and 2 columns
print(owner_df.shape) # There are 11 rows and 3 columns

print(dog_df.count(axis='columns'))
print(owner_df.count())

name_group = dog_df.groupby("name")["id"].count()
print(name_group)

