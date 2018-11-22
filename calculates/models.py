from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    # TODO: we should change the foreig key to band with many to many CharField
    # cause each project could have many band and each band could be in many project
    name = models.CharField(max_length=4, default='ABS')
    band = models.DecimalField(max_digits=4, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Panel(models.Model):
    # TODO: we should change the foreig key to panel with many to many CharField
    # cause each project could have many panel and each panel could be in many project
    name = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_name')
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + " (" + self.author.username + ")"

class Part(models.Model):
    ROTATION_CHOICES = (
    ('allowed', 'Allowed'),
    ('not_allowed', 'Not Allowed'),
    )
    length = models.DecimalField(max_digits=10, decimal_places=2, help_text='طول قطعه')
    length_band = models.IntegerField(default=0, help_text='تعداد نوار در طول')
    width = models.DecimalField(max_digits=10, decimal_places=2, help_text='عرض قطعه')
    width_band = models.IntegerField(default=0, help_text='تعداد نوار در عرض')
    quantity = models.IntegerField(default=1)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    rotation = models.CharField(max_length=20, choices=ROTATION_CHOICES, default='allowed' )
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.length) + ' * ' + str(self.width)
