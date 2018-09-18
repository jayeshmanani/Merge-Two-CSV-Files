#First Import pandas library as pd for ease of use
import pandas as pd

#Now read CSV file from your local location by using read_csv function of pandas library and save
# it to some variable here its df0
df0 = pd.read_csv('CSV/ratings.csv')

#Now read another CSV file from your local location by using read_csv function of pandas library
# and save it to some variable here its df1 and give it encoding='latin-1' only if it can't
# decode UTF-8 encoding
df1= pd.read_csv('CSV/movies.csv',encoding='latin-1')

#Use .head() function of pandas only if you want to see some data in the variable of type dataframe
# by default it takes value of first 5 but you can give some parameter to the function
# .head(10) will shows first 10 values from the dataframe

#print(df0.head())
#print(df1.head())

# use the merge function to merge csv files and give it parameter as shows below, on means the name of the column which
# is common on both csv files and can be used to jion both csv files data into one. and then save it to some variable
result = pd.merge(df1,
                 df0[['userId', 'movieId', 'rating','timestamp']],
                 on='movieId')

#print(result.head())

# .shape() function is used for know the shape of the data you are using, like the no. of columns and rows.
#print(df1.shape)
#print(df0.shape)

#print(result.shape)

# use the function .to_csv of the pandas library for saving the result of merged csv files to the new csv files.
result.to_csv('CSV/merged.csv')