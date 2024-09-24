from dictionary_of_movies import movies
def score(name):
    for i in movies:
        if name == i['name'] and i['imdb'] > 5.5:
            return True
    return False
print(score(input()))