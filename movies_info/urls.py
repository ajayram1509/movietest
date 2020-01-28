from django.conf.urls import url
from .import views




urlpatterns = [
    url(r'movies/',views.MovieView.as_view(),name='movies_ops'),
    url(r'setReview/',views.SetReview.as_view(),name='set_review'),
    url(r'rating/',views.RatingView.as_view(),name='rating_view'),
    url(r'setFavouriteGenre/',views.SetFavouriteGenre.as_view(),name='fav_genre'),
    url(r'voting/',views.VotingView.as_view(),name='voting_view'),
    url(r'getTopRatedMovies/',views.GetTopRatedMovies.as_view(),name='voting_view'),

 ]