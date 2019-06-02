from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL  # 'auth.User'


def set_delete_user():
    user_inner = get_user_model()
    return user_inner.objects.get_or_create(username='deleted')[0]  # get_or_create --> (obj, bool)


def limit_car_choices_to():
    # return {'is_staff': True}
    Q = models.Q
    return Q(username__icontains='x') | Q(username__icontains='e')


class Car(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET(set_delete_user),
                             limit_choices_to=limit_car_choices_to
                             )
    updated_by = models.ForeignKey(User, related_name='updated_car_user', null=True, blank=True)
    # on_delete=models.SET_NULL, null=True
    # on_delete=models.SET_DEFAULT, default=1

    # user = models.ForeignKey(User)
    # drivers = models.ManyToManyField(User)
    # first_owner = models.OneToOneField(User)
    # passengers = models.ManyToManyField(User)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

# ForeignKey = ManyToOneField() # Many users can have any car, car can only have one user

# car_obj = Car.objects.first()
# car_obj.user  # notation here
#
# User = car_obj.user.__class__
#
# abc = User.objects.all().last()  # filter queryset
#
# # below query sets are doing same thing
# user_cars = abc.car_set.all()  # reverse relationship
# user_cars_qs = Car.objects.filter(user=abc)  # forward relationship
#
#
# class Comment(models.Model):
#     user = models.ForeignKey(User)
#     content = models.CharField(max_length=120)
#
#
# comments = abc.comment_set.all()
# comments_qs = Comment.objects.filter(user=abc)
