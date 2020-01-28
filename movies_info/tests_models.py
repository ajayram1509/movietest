from django.test import TestCase
from accounts.models import User
from accounts.test import BaseCase
from movies_info.models import *
from decimal import Decimal
# Create your tests here.
class MoviesTest(BaseCase):

    def create_movie(self, movie_name='avengers',movie_genre='action',movie_year=2012):
        return Movies.objects.create(movie_name=movie_name,movie_genre=movie_genre,user=self.user,movie_year=movie_year)

    def test_movie_creation(self):
        movie = self.create_movie()
        self.assertTrue(isinstance(movie, Movies))
        self.assertEqual(movie.__str__(), movie.movie_name)


class ReviewTest(BaseCase):

    def create_review(self, review_text='test review'):
        return Review.objects.create(movie=self.movie,user=self.user,review_text=review_text)

    def test_review_creation(self):
        review = self.create_review()
        self.assertTrue(isinstance(review, Review))
        self.assertEqual(review.__str__(), review.movie.movie_name+"_"+review.review_text)

class RatingTest(BaseCase):

    def create_rating(self, rating_percentage=90):
        return Rating.objects.create(movie=self.movie,user=self.user,rating_percentage=rating_percentage)

    def test_rating_creation(self):
        rating = self.create_rating()
        self.assertTrue(isinstance(rating, Rating))
        self.assertEqual(rating.__str__(), rating.movie.movie_name+"_"+str(rating.rating_percentage))

class VotingTest(BaseCase):

    def create_voting(self, vote_type='Upvote'):
        return Voting.objects.create(movie=self.movie,user=self.user,voting_type=vote_type)

    def test_voting_creation(self):
        voting = self.create_voting()
        self.assertTrue(isinstance(voting, Voting))
        self.assertEqual(voting.__str__(), voting.movie.movie_name + "_" + voting.voting_type)

class FavouritesTest(BaseCase):

    def create_favourite(self, genre='action'):
        return Favourites.objects.create(user=self.user,genre=genre)

    def test_favourite_creation(self):
        fav = self.create_favourite()
        self.assertTrue(isinstance(fav, Favourites))
        self.assertEqual(fav.__str__(), str(fav.user.pk)+"_"+fav.genre)



