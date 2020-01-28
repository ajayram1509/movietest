import nose.tools as nt
from accounts.test import BaseCase
import json
import sys

class TestMovies(BaseCase):

    def test_Movies(self):
        path = '/movies/movies/'
        data = json.dumps({
            "movie_name": 'test',
            "genre": 'adventure',
            "movie_year": '2012'
        })
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.post(path, data, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n Movies Post : pass \n")
        nt.assert_equal(status, True)

    def test_movie_by_id(self):
        path = '/movies/movies/?movie_id=' + str(self.movie.pk)
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.get(path, {}, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n get Movie details by movie id: pass \n")
        nt.assert_equal(status, True)

    def test_movie_by_genere(self):
        path = '/movies/movies/?genere=action'
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.get(path, {}, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n get movie list by genre: pass \n")
        nt.assert_equal(status, True)

    def test_add_review(self):
        path = '/movies/setReview/'
        data = json.dumps({
            "review_text": 'test review',
            "movie_id": self.movie.pk
        })
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.post(path, data, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n Review Post : pass \n")
        nt.assert_equal(status, True)

    def test_rating(self):
        path = '/movies/rating/'
        data = json.dumps({
            "percentage": 90,
            "movie_id": self.movie.pk
        })
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.post(path, data, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n Rating Post : pass \n")
        nt.assert_equal(status, True)

    def test_voting(self):
        path = '/movies/voting/'
        data = json.dumps({
            "vote_type": 'Upvote',
            "movie_id": self.movie.pk
        })
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.post(path, data, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n Voting Post : pass \n")
        nt.assert_equal(status, True)

    def test_top_rated_movies(self):
        path = '/movies/getTopRatedMovies/'
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.get(path, {}, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n Top rated movies: pass \n")
        nt.assert_equal(status, True)

    def test_set_favourite_genre(self):
        path = '/movies/setFavouriteGenre/'
        data = json.dumps({
            "genre": 'action'
        })
        headers = {'HTTP_AUTHORIZATION': self.auth_token, 'content_type': 'application/json'}
        response = self.client.post(path, data, **headers)
        json_response = json.loads(response.content)
        status = json_response['status']
        if status == True:
            sys.stderr.write("\n set favourite genre : pass \n")
        nt.assert_equal(status, True)
