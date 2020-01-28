from django.db import models
from accounts.models import BaseModel
from django.conf import settings
from accounts.models import User
# Create your models here.

class Movies(BaseModel):
    GENER_CHOICES = (
        ('Action', 'action'),
        ('Adventure', 'adventure'),
        ('Comedy', 'comedy'),
        ('Romantic','Romantice')
    )
    movie_id=models.BigAutoField(primary_key=True)
    movie_name=models.CharField(null=True,blank=True,max_length=512)
    movie_genre = models.CharField(null=True, blank=True, max_length=32,choices=GENER_CHOICES)
    user=models.ForeignKey(User,related_name='movies',blank=True,null=True,on_delete=models.CASCADE)
    overallrating = models.DecimalField(
        max_digits=3, blank=True, null=True, decimal_places=1)
    movie_year=models.CharField(null=True,blank=True,max_length=4)
    def __str__(self):
        return self.movie_name

    def is_rated(self,user):
        try:
            obj=self.rating_movie.get(user=user)
            return True,obj.rating_percentage
        except:
            return False,0.0
    # def total_rating(self):
    #     obj=self.rating_movie.all()
    #     total_rating=0
    #     if obj:
    #         for i in obj:
    #             total_rating+=i.rating_percentage
    #         return total_rating/obj.count()
    #     else:
    #         return total_rating

    def is_voted(self,user):
        try:
            obj=self.voting_movie.get(user=user)
            return True,obj.voting_type
        except:
            return False,""

    def get_reviews(self):
        return [i.json() for i in self.review_movie.all()]


    def json(self,user=None):
        ret={}
        ret['movie_name']=self.movie_name
        ret['movie_genre']=self.movie_genre
        ret['movie_year']=self.movie_year
        ret['total_rating']=str(self.overallrating)
        if user:
            vote_stat,vote_type=self.is_voted(user)
            ret['is_voted']=vote_stat
            if vote_stat:
                ret['voted_type']=vote_type
            rating_stat,percentage=self.is_rated(user)
            ret['is_rated'] = rating_stat
            ret['rating_percentage']=percentage
        return ret

class Review(BaseModel):
    review_id = models.BigAutoField(primary_key=True)
    review_text = models.CharField(null=True, blank=True, max_length=512)
    user = models.ForeignKey(User, related_name='review_user', blank=True, null=True,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, related_name='review_movie', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.movie_name+"_"+self.review_text

    def json(self):
        ret={}
        ret['review_id']=self.review_id
        ret['review_text']=self.review_text
        return ret



class Rating(BaseModel):
    rating_id = models.BigAutoField(primary_key=True)
    rating_percentage = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='rating_user', blank=True, null=True,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, related_name='rating_movie', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.movie_name+"_"+str(self.rating_percentage)


class Voting(BaseModel):
    VOTE_CHOICES = (
        ('Downvote', 'downvote'),
        ('Upvote', 'upvote')
    )
    voting_id = models.BigAutoField(primary_key=True)
    voting_type = models.CharField(null=True, blank=True, max_length=32,choices=VOTE_CHOICES)
    user = models.ForeignKey(User, related_name='voting_user', blank=True, null=True,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, related_name='voting_movie', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.movie_name + "_" + self.voting_type
    def json(self):
        ret={}
        return ret

class Favourites(BaseModel):
    GENER_CHOICES = (
        ('Action', 'action'),
        ('Adventure', 'adventure'),
        ('Comedy', 'comedy'),
        ('Romantic', 'Romantice')
    )
    favourite_id = models.BigAutoField(primary_key=True)
    genre = models.CharField(null=True, blank=True, max_length=32, choices=GENER_CHOICES)
    user = models.ForeignKey(User, related_name='fav_genre', blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.pk)+"_"+self.genre