# Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame 
# #Obtain your data from the Codeup Data Science Database.



from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/titanic_db'
    
def get_db_url(user,password,host,database):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'

import pandas as pd
from env import user, password, host

get_titanic_data = pd.read_sql("select * from passengers", get_db_url(user, password, host, 'titanic_db'))

get_titanic_data


#Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
    
def get_db_url(user,password,host,database):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'

import pandas as pd
from env import user, password, host

get_iris_data = pd.read_sql("select * from species join measurements using(species_id)", get_db_url(user, password, host, 'iris_db'))


# Once you've got your get_titanic_data and get_iris_data functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for a local filename like titanic.csv or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.

df.to_csv("get_titanic_data.csv")

df.to_csv("get_iris_data.csv")