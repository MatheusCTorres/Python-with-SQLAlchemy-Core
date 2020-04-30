import sqlalchemy 

db = sqlalchemy.create_engine('mysql+mysqlconnector://root:@localhost/classicmodels')
conn = db.connect()
metadata = sqlalchemy.MetaData()

customers = sqlalchemy.Table('customers', metadata, autoload=True, autoload_with=db)

query = db.select([customers.columns.customerNumber,
                   customers.columns.customerName,
                   customers.columns.phone,
                   customers.columns.postalCode,
                   customers.columns.country]).where(customers.columns.customerName =='%s' % sys.argv[1])

ResponseProxy = connection.execute(query)

For r in ResponseProxy.fetchall():
print(r)