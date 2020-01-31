import pandas as pd

#######################################################################
#     Loading data into Pandas
#######################################################################

# df = pd.read_csv('pokemon_data.csv')
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(df)
# print(df.columns)

# print(df.head(3))
# print(df.tail(3))
# print(df_xlsx.head(3))


#######################################################################
#     Reading data in Pandas
#######################################################################

## Read Headers
# print(df.columns)

## Read Each Column
# print(df['Name'][0: 5])
# print(df[['Name', 'Type 1', 'HP']])
# print(df.Name)

## Read Each Row
# print(df.iloc[0:4])
# for index, row in df.iterrows():
#   print(index, row['Name'])
# print(df.loc[df['Type 1'] == 'Fire'])
# print(df.loc[df['Type 1'] == 'Grass'])

## Read a specific location (R,C)
# print(df.iloc[2,1])

#######################################################################
#     Sorting/Describing Data
#######################################################################

## Show scientific data
# print(df.describe())

## Sort data
# print(df.sort_values('Name', ascending=False))
# print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]))


#######################################################################
#     Making changes to the data
#######################################################################

# print(df.head(5))
# df['Total']=df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# df = df.drop(columns=['Total'])
# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# cols = list(df.columns.values)
# # print(cols)
# df = df[cols[0:4] + [cols[-1]] + cols[4:-1]]

# print(df.head(5))

#######################################################################
#     Output data to csv
#######################################################################

# df.to_csv('modified.csv', index=False)
# df.to_excel('modified.xlsx', index=False)
# df.to_csv('modified.txt', index=False, sep='\t')


#######################################################################
#     Filtering Data
#######################################################################

df.loc[df['Type 1'] == 'Grass']
print(df)
