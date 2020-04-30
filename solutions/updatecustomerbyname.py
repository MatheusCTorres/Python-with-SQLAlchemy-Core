import sqlalchemy 

db = sqlalchemy.create_engine('mysql+mysqlconnector://root:@localhost/classicmodels')
conn = db.connect()
metadata = sqlalchemy.MetaData()

customers = sqlalchemy.Table('customers', metadata, autoload=True, autoload_with=db)

query = db.update(customers).values(customerName=sys.argv[2],
phone=sys.argv[3], country=sys.argv[4])

query = query.where(customers.columns.customerNumber == sys.argv[1])

result = connection.execute(query)