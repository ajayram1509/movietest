from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from accounts.utils import httpResponseBadRequest,httpResponse,validate_data,percentage_validation
import json
# Create your views here.

class MovieView(APIView):
    def  get(self,request):
        data=request.GET
        user=request.user
        if 'movie_id' in data:
            try:
                obj=Movies.objects.get(pk=int(data['movie_id']))
                res=obj.json(user)
                res['reviews']=obj.get_reviews()
                return httpResponse(res)
            except Exception as e:
                return httpResponseBadRequest(error_description='No Movie Details Found with given id')
        elif 'genere' in data:
            ret = {}
            try:
                fav_genre=Favourites.object.get(user=user).genre
                movies_list=user.movies.filter(genre=fav_genre)
                ret['Favourite Movies'] = [i.json() for i in movies_list]
                return httpResponse(ret)
            except:
                ret['Favourite Movies'] = []
                return httpResponse(ret)

    def post(self,request):
        params=json.loads(request.body)
        req=['movie_name','genre','movie_year']
        error=validate_data(params,req)
        if error:
            return httpResponseBadRequest(error,"DATA MISSING")
        try:
            obj=Movies.objects.create(movie_name=params['movie_name'],movie_genre=params['genre'],movie_year=params['movie_year'],user_id=1)
            return httpResponse(obj.json())
        except Exception as e:
            return httpResponseBadRequest(error_description=e)

class SetReview(APIView):
    def post(self,request):
        params = json.loads(request.body)
        req=['review_text','movie_id']
        error=validate_data(params,req)
        if error:
            return httpResponseBadRequest(error,"Data Missing")
        try:
            Review.objects.create(review_text=params['review_text'], user_id=request.user.pk,movie_id=int(params['movie_id']))
            return httpResponse("success")
        except Exception as e:
            return httpResponseBadRequest(error_description=e)

class SetFavouriteGenre(APIView):

    def post(self,request):
        params=json.loads(request.body)
        if 'genre' not in params:
            return httpResponseBadRequest(error_description="Genre Required")
        try:
            Favourites.objects.create(genre=params['genre'],user_id=request.user.pk)
            return httpResponse("success")
        except Exception as e:
            return httpResponseBadRequest(error_description=e)


class RatingView(APIView):

    def post(self,request):
        params=json.loads(request.body)
        req=['percentage','movie_id']
        error=validate_data(params,req)
        if error:
            return httpResponseBadRequest(error, "DATA MISSING")
        percentage=params['percentage']
        check=percentage_validation(percentage)
        if check:
            return httpResponseBadRequest(check, "UNEXPECTED ERROR")
        try:
            Rating.objects.create(user_id=request.user.pk,rating_percentage=percentage,movie_id=int(params['movie_id']))
            return httpResponse("success")
        except Exception as e:
            return httpResponseBadRequest(error_description=e)



class VotingView(APIView):

    def post(self,request):
        params = json.loads(request.body)
        req = ['vote_type', 'movie_id']
        error = validate_data(params, req)
        if error:
            return httpResponseBadRequest(error, "DATA MISSING")
        try:
            Voting.objects.create(user_id=request.user.pk, voting_type=params['vote_type'],movie_id=int(params['movie_id']))
            return httpResponse("success")
        except Exception as e:
            return httpResponseBadRequest(error_description=e)

class GetTopRatedMovies(APIView):

    def get(self,request):
        try:
            obj=Movies.objects.filter(overallrating__gte=65).order_by('-overallrating')
            ret={}
            ret['Top Rated Movies']=[i.json() for i in obj]
            return httpResponse(ret)
        except Exception as e:
            return httpResponseBadRequest(error_description=e)