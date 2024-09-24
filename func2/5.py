from dictionary_of_movies import movies
def category(ctg):
    cat = []
    for i in movies:
        if ctg == i['category']:
            cat.append(i)
    all = 0
    num = len(cat)
    for i in cat:
        all += i['imdb']
    print(all/num)
category(input())