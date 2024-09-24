from dictionary_of_movies import movies
def avrg():
    all = 0
    num = len(movies)
    for i in movies:
        all += i['imdb']
    print(all/num)
avrg()
