# -*- coding: UTF-8 -*-


import pandas
import Recommenders
from sklearn.model_selection import train_test_split


def music_recommend(song_name, id_num):
    triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
    songs_metadata_file = 'song_data.csv'
    song_df_1 = pandas.read_table(triplets_file, header=None)
    song_df_1.columns = ['user_id', 'song_id', 'listen_count']
    song_df_2 = pandas.read_csv(songs_metadata_file)

    song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

    # with open("song_df.head().txt", "w") as song_df_head:
    #     song_df_head.write((song_df.head()).encode("utf-8"))
    # print(song_df.head())

    song_grouped = song_df.groupby(['title']).agg({'listen_count': 'count'}).reset_index()
    grouped_sum = song_grouped['listen_count'].sum()
    song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum)*100
    song_grouped.sort_values(['listen_count', 'title'], ascending=[0, 1])
    # with open("song_grouped.txt", "w") as grouped_song:
    # print(song_grouped)

    #######################################
    users = song_df['user_id'].unique()
    # len(users)
    songs = song_df['title'].unique()
    # len(songs)

    train_data, test_data = train_test_split(song_df, test_size=0.20, random_state=0)

    pm = Recommenders.popularity_recommender_py()
    pm.create(train_data, 'user_id', 'title')


    # user_id = users[5]
    # pm.recommend(user_id)
    # with open("recommend_user_id.txt", "w"):
    # print(pm.recommend(user_id))

    is_model = Recommenders.item_similarity_recommender_py()

    is_model.create(train_data, 'user_id', 'title')
    num = id_num
    user_id = users[num]
    user_items = is_model.get_user_items(user_id)
    # user_items = is_model.get_similar_items([song_name])
    print(user_items)
    print("------------------------------------------------------------------------------------")
    print("Training data songs for the user user id: %s:" % user_id)
    print("Training data songs for the user select: %s:" % song_name)
    print("------------------------------------------------------------------------------------")
    a = 0
    for user_item in user_items:
        print(user_item)
        a += 1
        if a is 10:
            break


    num = len(user_items)
    print("----------------------------------------------------------------------")
    print("Recommendation process going on:")
    print("Totle recommendation music : %s " % a)
    print("----------------------------------------------------------------------")


    # print(is_model.recommend(user_id))
    #
    # print(is_model.get_similar_items(['U Smile']))
    quit()


