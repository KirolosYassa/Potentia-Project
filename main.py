import requests
import csv
import pandas as pd

# Read the csv file
movies_pd = pd.read_csv("Movies title.csv")

# Print it out if you want
# print(movies_pd)
movies = []

for index, row in movies_pd.iterrows():
    # print(row["Title"])
    movies.append(row["Title"])

print(movies)


# key = ""
# movieTitle = ""

# url = f"http://www.omdbapi.com/?apikey={key}&title={movieTitle}"
# response = requests.get(url)
# print(response)
