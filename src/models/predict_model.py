import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


import joblib
import requests



MOVIES = r'models\movies_with_poster.pkl'
SIM_MATRIX = r'models\similarity_matrix.pkl'



movies_df = joblib.load(MOVIES)
sim_martix = joblib.load(SIM_MATRIX)



def get_top_n_movies(n):
    '''
    This fun return movies recommendation based on popularity
    '''
    df = movies_df.sort_values(by=[ 'num_of_vote' , 'vote_average' ], ascending=False).head(n)
    return df

print(get_top_n_movies( n = 20))




def recommmendation_by_id(movie_id):   

    try: 
        recomm_movies= pd.DataFrame(sim_martix[movie_id].sort_values(ascending=True).head(10)).reset_index()[1:]
        recom_df = pd.DataFrame(columns=movies_df.columns)
        for title in recomm_movies['title']:
            recom =  movies_df[movies_df['title'] == title] 
            recom_df = pd.concat([recom_df , recom])
        return recom_df
    except KeyError:
        print('Movie not found in the similarity matrix. Please choose another movie.')

# print(recommmendation_by_id(55555555555555555))