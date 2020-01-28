from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from movies_info.models import Movies,Rating



@receiver(post_save, sender=Rating)
def add_rating_signal(sender, instance=None, **kwargs):
    if not instance:
        return False
    if sender == Rating:
        try:
            total=0
            obj = Rating.objects.filter(movie_id=instance.movie.pk)
            for i in obj:
                total+=i.rating_percentage
            total=total/obj.count()
            instance.movie.overallrating=total
            instance.movie.save()
        except Exception as e:
            pass

