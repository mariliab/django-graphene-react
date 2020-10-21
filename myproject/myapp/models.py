from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EducationModel(models.Model):
    name = models.CharField(max_length=100)
    education_type = models.CharField(max_length=100)
    education_length = models.CharField(max_length=100)
    education_pace = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name