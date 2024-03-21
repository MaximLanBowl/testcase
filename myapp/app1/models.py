from django.db import models


class User(models.Model):
    objects = None
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


class RefCode(models.Model):
    objects = None
    code = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(User, related_name='ref_code', on_delete=models.CASCADE)
    before_date = models.DateField()


class Ref(models.Model):
    objects = None
    refer = models.ForeignKey(User, related_name='refer', on_delete=models.CASCADE)
    refed = models.ForeignKey(User, related_name='refed', on_delete=models.CASCADE)


