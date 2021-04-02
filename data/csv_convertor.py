import os
import pandas as pd
# import sqlalchemy

#create the engine to connect to the PostgreSQL database?
# engine = sqlalchemy.create_engine("postgresql+psycopg2://:.@localhost/mydb")
# ('postgresql://postgres:test1234@localhost:5432/sql-shack-demo')

#read data from CSV and load into a dataframe object
test = pd.read_csv('CA_download_03-26-2021.csv')


# Table rename not working
# test.rename(columns = {'case_number', 'dlc', 'lname', 'fname', 'age_missing', 'city', 'county', 'age', 'sex', 'race', 'date_modified'}, inplace = True)

#write data into the table in PostgreSQL database
# test.to_sql('childrencsv', engine)

# with open('CA_download_03-26-2021.csv') as test:
#      print(test)# 