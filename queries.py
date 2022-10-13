#pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()


def directors_count(db):
    # return the number of directors contained in the database
    db.execute("SELECT COUNT(name) FROM DIRECTORS")
    result = db.fetchall()
    print(result)
    return result[0][0]
directors_count(db)

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("SELECT name FROM directors ORDER by name ASC")
    result1 = db.fetchall()
    #print(result1)
    name_list = [tuple[0] for tuple in result1]
    return name_list
directors_list(db)

def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db.execute("""
        SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
    """)
    result2 = db.fetchall()
    return [movie[0] for movie in result2]


love_movies(db)


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    #name = input("name?\n>")
    query = "select count(*) from directors where name like ?"
    db.execute(query,(f'%{name}%',))
    results3 = db.fetchone()
    print(results3)
    return results3[0]
#directors_named_like_count(db, "blah")

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    #min_length = input("duration?\n>")
    query = "select title from movies where minutes> ?order by title asc"
    db.execute(query,(min_length,))
    results = db.fetchall()
    return [movie[0] for movie in results]
#movies_longer_than(db, 30)
