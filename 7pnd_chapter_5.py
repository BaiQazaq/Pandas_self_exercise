# Performing operations on DataFrame objects and its contents
import pandas as pd 

sp500 = pd.read_csv("Notebooks/Data/sp500.csv", #read the data
                    index_col="Symbol",         #use as a index column Symbol
                    usecols=[0, 2, 3, 7])       #read and show the next columns 0, 2, 3, 7

                    #Renameing of the columns
print()
print('Renameing of the columns')
print('*'*80)

# by method - .rename(). This method returns new DataFrame with renamed column with copyed data from initial DataFrame
#next code will rename the column "Book Value" to the "BookValue" (without space between words)

newSP500 = sp500.rename(columns={'Book Value': 'BookValue'})
print(newSP500[:2])

#next code prove that initial dataframe sp500 did not changed
print(sp500.columns)

#for renameing columns on initial DataFrame without creating new dataframe usualy use the parameter -
# - inplace=True
#code below show it

sp500.rename(columns=
                   {'Book Value': 'BookValue'}, 
                   inplace=True)
print(sp500.columns)

#return to initial condition for using initial datafrane further
sp500.rename(columns=
                   {'BookValue': 'Book Value'}, 
                   inplace=True)

                # Adding new columns by operator [] and method .insert()
print()
print('Adding the columns')
print('*'*80)

#for manipulation copying the dataframe
sp500_copy = sp500.copy()

#adding column by []. Adding the column 'RoundedPrice' which equal to the rounded value of the column
# 'Price' from sp500. New column adds to the end of columns
sp500_copy['RoundedPrice'] = sp500.Price.round()
print(sp500_copy[:2])

#for adding column to a certain position should use the method - .insert()
copy = sp500.copy()
copy.insert(1, 'RoundedPrice', sp500.Price.round())
print(copy[:2])