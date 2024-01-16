# Performing operations on DataFrame objects and its contents
import pandas as pd
import numpy as np

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
print("*"*30)

#for adding column to a certain position should use the method - .insert()
copy = sp500.copy()
copy.insert(1, 'RoundedPrice', sp500.Price.round())
print(copy[:2])
print("*"*30)

#Adding columns due to expansion of DataFrame by .loc[] and []
# creating copy by a slice
ss = sp500[:3].copy()
# adding column with 0 values
ss.loc[:, 'PER'] = 0
print(ss)
print("*"*30)

#adding column with randomly generated values
# creating copy by a slice
ss = sp500[:3].copy()
# ganerating values and addiing the column 'REP'
np.random.seed(123456)
ss.loc[:, 'REP'] = pd.Series(np.random.normal(size=3), index=ss.index)
print(ss)
print("*"*30)

# adding column due to a concatenation
# if need create new dataframen with new columns and no change a initial dataframe use pd.concat()
# pd.concat() create new dataframe
# next code create new dataframe with only one column contain rounded price values
# axis-1 point that object of dataframe have to concantenate by axis of columns
# if we need concantenate by rows we should use axis=0

#creating object of dataframe with one column 'RoundedPrice'
rounded_price = pd.DataFrame({'RoundedPrice': sp500.Price.round()})

# concatenation by axis of columns
concantenated = pd.concat([sp500, rounded_price], axis=1)
print(concantenated[:5])
print("*"*30)

# concantenate allow duplication the labels(names) of columns 
rounded_price = pd.DataFrame({'Price': sp500.Price.round()})
print(rounded_price[:5])

dups = pd.concat([sp500, rounded_price], axis=1)
print(dups[:5])
print("*"*30)

# curiously by attribute .Price we can exctract both columns Price, which show a code below
print(dups.Price[:5])

                        # REORDERING of columns
print()
print('Reordering of columns')
print('*'*80)
# reordering can be do it with selection by []
reversed_column_names = sp500.columns[::-1]
print(reversed_column_names)
print()
print(sp500[reversed_column_names][:5])
print()

# Editing the values of columns
       # by [] (this action will change initial dataframe)
copy = sp500.copy()  # copy for avoiding change the initial dataframe
# change values of column Price to the new values instead of adding new
copy.Price = rounded_price.Price
print(copy[:5])

# furthermore the values of columns can be replace on initial dataframe by slice
copy1 = sp500.copy()  # copy for avoiding change the initial dataframe
copy1.loc[:, 'Price'] = rounded_price.Price
print(copy1[:5])
print()

                        #Deleting columns
# del, .pop(), .drop()
#  del delete the Series from dataframe, initial dataframe will changed
#  .pop() delete and return Series, initial dataframe will changed
#  .drop(labels, axis=1) return new dataframe, and initial dataframe stay 
               # del
copy = sp500.copy()
print(copy.columns)
del copy['Book Value']
print('del ')
print(copy[:2])
print()

               # .pop()

copy = sp500.copy()
popped = copy.pop('Sector')
print(popped) #show deleted Series
print('.pop() method')
print(copy[:2])
print()

               # .drop()
copy = sp500.copy()
afterdrop = copy.drop(['Sector'], axis=1)
print('.drop() method')
print(afterdrop[:5])
print()

                  # Join new rows

# ._append()  return new dataframe
# NOTE: As of Pandas version 2.0, the .append() method is no longer in use. 
# It is important to keep this in mind while working with Pandas. 
# More efficient alternatives for concatenating DataFrames are the .concat() function 
# from the pandas.DataFrame module.

df1 = sp500.iloc[0:3].copy()
df2 = sp500.iloc[[10, 11, 2]]
appended = df1._append(df2)
print("._append() method")
print(appended)
print()

# join rows when dataframe's count of columns not equal 

df3 = pd.DataFrame(0.0, index=df1.index, columns=['PER'])
print("df3 dataframe")
print(df3)
print()

df1._append(df3, sort=True)  # sort=True - alphabetical sorting 
                             # sort=False - add columns to the end
print("df1 appended df3")
print(df1)
print()

                     #CONCATENATING rows

# pd.concat and axis=0

df11 = sp500.iloc[0:3].copy()
df22 = sp500.iloc[[10, 11, 2]]
concat_rows = pd.concat([df11, df22])
print("concantenated pd")
print(concat_rows)
print()

# when collection of columns on dataframes do not correspond new dataframe will has values NAN

df2_2 = df22.copy()
df2_2.insert(3, 'Foo', pd.Series(0, index=df2.index))
print("DF2_2")
print(df2_2)
print()
concat_rows_foo = pd.concat([df11, df2_2], sort=True)
print("1 Concanated with absent columns")
print(concat_rows_foo)
print()

concat_rows_foo = pd.concat([df11, df2_2], keys=['df11', 'df2'], sort=True)
print("2 Concanated with absent columns")
print(concat_rows_foo)
print()

                     #Adding and replacing rows by axpanding datframe

#creating slice of dataframe
ss = sp500[:3].copy()
#creating a new row with label FOO and giving some values by list
ss.loc['FOO'] = ['the sector', 100, 110] #it change the initial dataframe
print("SS")
print(ss)
print()

                     #deleting rows by method .drop()

zz = sp500[:5]
print("ZZ")
print(zz)
print()

afterdrop1 = zz.drop(['ABT', 'ACN'])
afterdrop1[:5]
print("AFTERDROP1")
print(afterdrop1)
print()
                     #deleting rows by logical selecting

selection1 = sp500.Price > 300
print(len(selection1), selection1.sum())
print(sp500[sp500.Price > 300])

price_less_than_300 = sp500[~selection1] #tilde ~ is a bitwise operator. 
                                         # If the operand is 1, it returns 0, and if 0, it returns 1.
print(price_less_than_300)

                     #deleting rows by slice
only_first_three = sp500[:3].copy()
print(only_first_three)