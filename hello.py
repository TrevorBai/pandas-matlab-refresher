import pandas as pd
import re

#######################################################################
#     Loading data into Pandas
#######################################################################

# df = pd.read_csv('pokemon_data.csv')
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# df = pd.read_csv('pokemon_data.txt', delimiter='\t')

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


# use Bitwise AND "&" instead of Boolean AND "and"
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# # df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
# # new_df.to_csv('filtered.csv')
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)

# print(df.loc[df['Name'].str.contains('Mega ')])
# print(df.loc[~df['Name'].str.contains('Mega ')])
# print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
# print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])


#######################################################################
#     Conditional Changes
#######################################################################

# df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
# print(df)


#######################################################################
#     Aggregate Statistics (Groupby)
#######################################################################

# df = pd.read_csv('modified.csv')
# print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))
# print(df.groupby(['Type 1']).sum())
# df['count'] = 1
# print(df)

# print(df.groupby(['Type 1', 'Type 2']).count()['count'])


#######################################################################
#     Working with large amounts of data
#######################################################################
df = pd.read_csv('modified.csv')
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv', chunksize=5):
  results = df.groupby(['Type 1']).count()
  new_df = pd.concat([new_df, results], sort=False)
print(new_df)
