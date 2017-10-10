from django.db import models


class MostWatched(models.Model):
    """
    Netflix Model
    Defines the attributes of a most-watched movie use case
    """
    user_id = models.IntegerField()
    details_id = models.IntegerField()
    location_id = models.IntegerField()
    plan_id = models.IntegerField()
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length = 50)
    genre_id = models.IntegerField()
    director_id = models.IntegerField()
    movie_cast = models.CharField(max_length = 50)
    release_id = models.IntegerField()

class SalesPerLocation(models.Model):
    """
    Netflix Model
    Defines the attributes of a sales volume as per location use case
    """
    location_id = models.IntegerField()
    location_city = models.CharField(max_length = 50)
    location_state = models.CharField(max_length = 50)
    location_name = models.CharField(max_length = 50)
    payment_id = models.IntegerField()
    payment_type = models.CharField(max_length = 50)
    payment_amount = models.IntegerField()

class GenrePreference(models.Model):
    """
    Netflix Model
    Defines the attributes of a user genre preference use case
    """   
    user_id = models.IntegerField()
    details_id = models.IntegerField()
    location_id = models.IntegerField()
    plan_id = models.IntegerField()
    genre_id = models.IntegerField()
    genre_soap = models.CharField(max_length = 50)
    genre_movie = models.CharField(max_length = 50)

class AverageViewHour(models.Model):
    """
    Netflix Model
    Defines the attributes of users average view hour use case
    """
    user_id = models.IntegerField()
    details_id = models.IntegerField()
    location_id = models.IntegerField()
    plan_id = models.IntegerField()
    soap_id = models.IntegerField()
    soap_title = models.CharField(max_length = 50)
    genre_id = models.IntegerField()
    director_id = models.IntegerField()
    soap_cast = models.CharField(max_length = 50)
    release_id = models.IntegerField()
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length = 50)
    genre_id = models.IntegerField()
    director_id = models.IntegerField()
    movie_cast = models.CharField(max_length = 50)
    release_id = models.IntegerField()

class PaymentContinuity(models.Model):
    """
    Netflix Model
    Defines the attributes of payment continuity i.e. whether users are continuing payment and renewal of subscription movie use case
    """
    plan_id = models.IntegerField()
    payment_id = models.IntegerField()
    payment_id = models.IntegerField()
    payment_type = models.CharField(max_length = 50)
    payment_amount = models.IntegerField()
     user_id = models.IntegerField()
    details_id = models.IntegerField()
    location_id = models.IntegerField()
    plan_id = models.IntegerField()


