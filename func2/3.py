from dictionary_of_movies import movies
def category(ctg):
    my_list = []
    for i in movies:
        if ctg == i['category']:
            my_list.append(i)
    print(my_list)
category(input())