# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#ex1
from movies import movies
def score_above(movie):
    score = True
    for mov in movies:
        if mov['name'] == movie and mov['imdb'] > 5.5:
            score = True
        elif mov['name'] == movie and mov['imdb'] < 5.5:
            score = False
    return score
print(score_above(input()))

#ex2
from movies import movies
def movies_above(*movies):
    result = []
    for mov in movies:
        if mov['imdb'] > 5.5:
            result.append(mov['name'])
    return result
print(*movies_above(*movies), sep = '\n')

#ex3
from movies import movies
def category_sort(category):
    result = []
    for mov in movies:
        if mov['category'] == category:
            result.append(mov['name'])
    return result
category = input()
print(*category_sort(category), sep = '\n')

#ex4
from movies import movies
def average_imdb(*movies):
    sum = 0
    for mov in movies:
        sum += float(mov['imdb'])
    return sum/len(movies)
print(average_imdb(*movies))

#ex5
from movies import movies
def average_of_category(category):
    sum = 0
    cnt = 0
    for mov in movies:
        if mov['category'] == category:
            sum += float(mov['imdb'])
            cnt += 1
    return sum / cnt
print(average_of_category(input()))