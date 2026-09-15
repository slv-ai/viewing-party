# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title":title,
            "genre" : genre,
            "rating" : rating
        }
    else:
        return None
def add_to_watched(user_data,movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data,title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    count = len(user_data['watched'])
    total = 0
    movies = user_data['watched']
    if not movies:
        return 0.0
    
    for movie in movies:
        total += movie['rating']
    return float(total / count)
    
def get_most_watched_genre(user_data):
    
    freq_map ={}
    movies = user_data['watched']
    if not movies:
        return None
    for movie in movies:
        genre = movie['genre']
        if genre not in freq_map:
            freq_map[genre] = 1
        else:
            freq_map[genre] += 1

    max_count =0
    most_watched = " "
    for genre, count in freq_map.items():
        if count > max_count:
            max_count =count
            most_watched = genre
    return most_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_list =[]
    user_watched_list = user_data['watched']
    friends_watched_list =[]
    friends = user_data['friends']
    for friend in friends:
        for movie in friend['watched']:
            friends_watched_list.append(movie['title'])
    for movie in user_watched_list:
        if movie['title'] not in friends_watched_list:
            unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    user_watched_movies = []
    for movies in user_data['watched']:
        user_watched_movies.append(movies['title'])
    unique_movies=[]
    friends = user_data['friends']
    for friend in friends:
        for movies in friend['watched']:
            if movies['title'] not in user_watched_movies:
                if movies['title'] not in [movie['title'] for movie in unique_movies]:
                    unique_movies.append(movies)

    return unique_movies
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies =[]
    movies_list = get_friends_unique_watched(user_data)
    for movie in movies_list:
        if movie['host'] in user_data['subscriptions']:
            recommended_movies.append(movie)
    return recommended_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommeded_movies =[]
    genre =get_most_watched_genre(user_data)
    movie_list = get_friends_unique_watched(user_data)
    for movie in movie_list:
        if movie['genre'] == genre:
            recommeded_movies.append(movie)
    return recommeded_movies

def get_rec_from_favorites(user_data):
    recommended_movies =[]
    friends_watched_movies =[]
    #print(user_data)
    friends = user_data['friends']
    for friend in friends:
        for movie in friend['watched']:
            if movie['title'] not in friends_watched_movies:
                friends_watched_movies.append(movie['title'])
    print(friends_watched_movies)
    for movies in user_data['favorites']:
        if movies['title'] not in friends_watched_movies:
            recommended_movies.append(movies)
    #print(recommended_movies)
    return recommended_movies

