# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
# netflix_df = pd.read_csv("netflix_data.csv")
netflix_df = pd.read_csv("")
print(netflix_df.head(5))
# filter for movies only
# movies = netflix_df[netflix_df['type']=='Movie']
# # filter movies in 1990's
# movies_in_1990 = movies[movies['release_year'].between(1990, 1999)]
# most_frequent_movies_in_1990s= movies_in_1990['duration'].mode()[0]
# duration = int(most_frequent_movies_in_1990s)
# Frequent = "the most frequent movie duration in the 1990s = {duration}s"
# print(f'frequent')
# # Generate a list of all action_movies durations
# action_movies_in_1990 = movies_in_1990[movies['genre']== 'Action']
# action_movies_in_1990s_list = action_movies_in_1990['duration'].tolist()

# # filter and count short action movies duration < 90
# short_movies = [movie for movie in action_movies_in_1990s_list if movie < 90]
# short_movie_count = len(short_movies)
# print(short_movies_count)