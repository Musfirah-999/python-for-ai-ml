import pandas as pd
import openpyxl as oxl
# df = pd.read_csv('pokemon_data.csv')
# print(df)
# print(f"-----First df.head(5): {df.head(5)}")
# print(f"-----Last df.tail(3): {df.tail(3)}")

# df = pd.read_excel('pokemon_data.xlsx')
# print(df)
# print(f"-----First df.head(5): {df.head(5)}")
# print(f"-----Last df.tail(3): {df.tail(3)}")

df = pd.read_csv('pokemon_data.txt' , delimiter='\t')
print(df)
print(f"-----First df.head(5): {df.head(5)}")
print(f"-----Last df.tail(3): {df.tail(3)}")