import pandas as pd
import openpyxl as oxl
# df = pd.read_csv('pokemon_data.csv')
# print(df)
# print(f"-----First df.head(5): {df.head(5)}")
# print(f"-----Last df.tail(3): {df.tail(3)}")

df = pd.read_excel('pokemon_data.xlsx')
# print(df)
# print(f"-----First df.head(5): {df.head(5)}")
# print(f"-----Last df.tail(3): {df.tail(3)}")

# df = pd.read_csv('pokemon_data.txt' , delimiter='\t')
# print(df)
# print(f"-----First df.head(5): {df.head(5)}")
# print(f"-----Last df.tail(3): {df.tail(3)}")

# print(df.columns)
# print(df[['Name', 'Type 1']][0:5])
# print(df.head(5))

# print(df.iloc[2:5])  # rows 2 to 4
# print(df.iloc[2, 1])  # row 2, column 1
# print(df.iloc[1])  # row 1
# print(df.iloc[1:4, 2:4])  # rows 1 to 3, columns 2 to 3
# print(df.iloc[2,1])  # row 2, column 1

# for index, row in df.iterrows():
#     print(index, row['Name'])

print(df.loc[df['Type 1'] == 'Fire'])

