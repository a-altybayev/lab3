from dictionary_of_movies import movies
def list():
    my_list = []
    for i in movies:
        if int(i['imdb']) > 5.5:
            my_list.append(i)
    print(my_list)
list()