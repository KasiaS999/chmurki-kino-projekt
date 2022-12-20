from flask import Flask, render_template, request, flash, redirect, url_for
from functions import *
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


def rearrange_people_list(ppl):
    new_dir = {}
    for elem in ppl:
        new_dir[elem['p']['name']] = {'r': elem['r'][1],
                                      'name': elem['p']['name']}
    return new_dir


@app.route('/actors', methods=['GET', 'POST'])
def people():
    ppl = rearrange_people_list(list_all_people())
    return render_template('people.html', people=ppl)


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    mov = list_all_movies()
    return render_template('movies.html', movies=mov)


@app.route('/movie_info', methods=['GET', 'POST'])
def movie_info():
    if request.method == 'POST':
        title = request.form['title']
        info = find_and_return_movie(title)
        if not info:
            flash("Upps, there is no information about this movie in "
                  "this database :(")
        else:
            tagline = info[0]['n']['tagline']
            released = info[0]['n']['released']
            title = info[0]['n']['title']
            return render_template('list_movie_info.html', title=title,
                                   released=released, tagline=tagline)
    return render_template('search_movie_info.html')


def check_if_year_str_converts_to_int(year):
    try:
        int(year)
        return True
    except ValueError:
        return False


@app.route('/movies_year', methods=['GET', 'POST'])
def movies_year():
    if request.method == 'POST':
        year = request.form['year']
        if not check_if_year_str_converts_to_int(year):
            flash(f"There is something from with year: {year}. Try again.")
            return render_template('search_movie_by_year.html')
        info = find_and_return_movies_year(year)
        if not info:
            flash(f"Upps, there is no information about movies released in "
                  f"{year} in this database.")

        else:
            mov = find_and_return_movies_year(year)
            return render_template('list_movies_from_year.html', movies=mov,
                                   year=year)

    return render_template('search_movie_by_year.html')


@app.route('/movie_actors', methods=['GET', 'POST'])
def movie_actors():
    if request.method == 'POST':
        title = request.form['title']
        act = find_movie_actors(title)
        if not act:
            flash("Upps, there is no information about this movie in "
                  "this database :(")
        else:
            return render_template('list_actors_from_movie.html', actors=act,
                                   movie=title)
    return render_template('search_movie_info.html')


@app.route('/movie_cast', methods=['GET', 'POST'])
def movie_cast():
    if request.method == 'POST':
        title = request.form['title']
        cast = find_cast(title)
        if not cast:
            flash("Upps, there is no information about this movie in "
                  "this database :(")
        else:
            return render_template('list_movie_cast.html', cast=cast,
                                   movie=title)
    return render_template('search_movie_info.html')


@app.route('/person_in_movies', methods=['GET', 'POST'])
def person_in_movies():
    if request.method == 'POST':
        person = request.form['person']
        movies_and_relations = find_persons_movies(person)
        if not movies_and_relations:
            flash("Upps, there is no information about this person in "
                  "this database :(")
        else:
            return render_template('list_persons_role.html',
                                   roles=movies_and_relations, person=person)
    return render_template('search_person_info.html')


@app.route('/movie_director', methods=['GET', 'POST'])
def movie_director():
    if request.method == 'POST':
        title = request.form['title']
        director = find_movie_director(title)
        if not director:
            flash("Upps, there is no information about this movie in "
                  "this database :(")
        else:
            return render_template('movie_director.html', director=director,
                                   movie=title)

    return render_template('search_movie_info.html')

