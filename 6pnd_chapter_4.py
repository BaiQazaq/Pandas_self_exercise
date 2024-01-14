import pandas as pd
# creating DataFrame object by csv file

sp500 = pd.read_csv("Notebooks/Data/sp500.csv", #read the data
                    index_col="Symbol",         #use as a index column Symbol
                    usecols=[0, 2, 3, 7])       #read and show the next columns 0, 2, 3, 7

#will print the first 5 rows by method "head"

print(sp500.head())

#check the lenghth of this DataFrame

print(f"Length of DataFrame is {len(sp500)} rows")

#forms of DataFrame

print(f"Rows = {sp500.shape[0]} and Colums = {sp500.shape[1]}")

# size of DataFrame
print(f"Size of DataFrame = {sp500.size}")

# indexes of DataFrame
print(f"List of indexes: \n {sp500.index}")

# columns name (index) of DataFrame
print(f"Columns title: \n {sp500.columns}")


                    #SELECT the COLUMNS
print()
print('SELECT the COLUMNS')
print('*'*80)
# selecting a specific column(s) from object of DataFrame execute with operator "[]". 
# next code exctract the column with name "Sector" first 5 rows

print(f"Datas from columns \"Sector\": \n {sp500['Sector'].head()}")

# when from DataFrame object select only one column result will object of Series
print(type(sp500['Sector']))

# selecting few columns by list of name of columns
print(sp500[['Price', 'Book Value']].head())

# furthermore columns can be selected by attributes if the name of columns has not space
print(sp500.Price)
# same code will not work with column name 'Book Value', because the name include the space


                    # SELECT the ROWS
print()
print('SELECT the ROWS')
print('*'*80)
#the rows can be selected by attribute - .loc[]
# exctracting the row with index 'MMM', will return the Series object
print(sp500.loc['MMM'])

# moreover the few rows we can extract by list of index
print(sp500.loc[['MMM', 'MSFT']])

#also rows can be extracted by attribute - .iloc[]
# extracting the rows with index 0 and 2

print(sp500.iloc[[0, 2]])

#the first we can indentification of the index via label of index
i1 = sp500.index.get_loc('MMM')
i2 = sp500.index.get_loc('A')
print(i1, i2)
print(sp500.iloc[[i1, i2]])

                        #SELECT the SCALAR VALUE
print()
print('SELECT the SCALAR VALUE')
print('*'*80)

# by attribute - .at[]
print(sp500.at['MMM', 'Price'])

# by attrimute - .iat[]
print(sp500.iat[0, 1])

                        #SELECTING the SLICE
print()
print('SELECT the SLICE')
print('*'*80)

#by attribute - [], slice will generat (select) by index of rows
print(sp500[:5])  #select the first 5 rows

#next code will return the rows from 'ABT' to 'ACN'
print(sp500['ABT':'ACN'])

                        #LOGICAL SELECT of rows
print()
print('LOGICAL SELECT of rows')
print('*'*80)

#logical attributs - <, >
print(sp500.Price < 100) #will return all result as bool value: False or True

print(sp500[sp500.Price < 100]) #will return value True as a DataFrame 

#by using () availble unite few logical conditions
#next code will return rows with value of the column Price from 6 to 10
r = sp500[(sp500.Price < 10) &
            (sp500.Price > 6)]['Price']
print(r)

#usualy use few variables for logical exctracting
#next code show and extract all rows where variable (column lable) "Sector" equal "Health Care" 
# and column(variable) "Price" more or equal 100
r = sp500[(sp500.Sector == 'Health Care') & (sp500.Price > 100)][['Price', 'Sector']]

print(r)

                                #Simultaneously selecting rows nad columns
print()
print('Simultaneously SELECT of rows and columns')
print('*'*80)

#selecting the rows with lables 'ABT' and 'ZTS' for the columns 'Sector' and 'Price'
r = sp500.loc[['ABT', 'ZTS']][['Sector', 'Price']]
print(r)
