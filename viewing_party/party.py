# ----------- HELPER FUNCTIONS ------------
def get_friends_watched_movies(user_data):
    """Return a list of all movies watched by the user's friends."""
    friends_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)

    return friends_movies

def get_movie_titles(movies):
    """Return a list of movie titles from a list of movie dictionaries."""
    titles = []

    for movie in movies:
        titles.append(movie["title"])

    return titles

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
    """Calculate the average rating of all movies the user has watched."""
    count = len(user_data['watched'])
    total = 0
    movies = user_data['watched']
    if not movies:
        return 0.0
    
    for movie in movies:
        total += movie['rating']
    return float(total / count)
    
def get_most_watched_genre(user_data):
    """Find the genre that appears most often in the user's watched list."""
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

    """Return movies the user watched that none of their friends watched."""

    user_movies = user_data["watched"]
    friends_movies = get_friends_watched_movies(user_data)
    friends_titles = get_movie_titles(friends_movies)

    unique_movies = []

    for movie in user_movies:
        if movie["title"] not in friends_titles:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):

    """Return movies friends watched that the user has not watched."""

    user_movies = user_data["watched"]
    friends_movies = get_friends_watched_movies(user_data)

    user_titles = get_movie_titles(user_movies)

    unique_movies = []

    for movie in friends_movies:
        if movie["title"] not in user_titles:
            if movie["title"] not in get_movie_titles(unique_movies):
                unique_movies.append(movie)

    return unique_movies

    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """Return movies friends watched that are available on the user's subscriptions."""
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
    """Return movies friends watched that match the user's most-watched genre."""
    recommeded_movies =[]
    genre =get_most_watched_genre(user_data)
    movie_list = get_friends_unique_watched(user_data)
    for movie in movie_list:
        if movie['genre'] == genre:
            recommeded_movies.append(movie)
    return recommeded_movies

def get_rec_from_favorites(user_data):
    """Return favorite movies that none of the user's friends have watched."""
    recommended_movies =[]
    friends_watched_movies = get_friends_watched_movies(user_data)
    titles = get_movie_titles(friends_watched_movies)

    for movies in user_data['favorites']:
        if movies['title'] not in titles:
            recommended_movies.append(movies)
    return recommended_movies

