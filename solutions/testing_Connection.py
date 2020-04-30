import sqlalchemy

db = sqlalchemy.create_engine('mysql+mysqlconnector://root:@localhost/classicmodels')
conn = db.connect()
metadata = sqlalchemy.MetaData()

customers = sqlalchemy.Table('customers', metadata, autoload=True, autoload_with=db)

print(customers.columns.keys())