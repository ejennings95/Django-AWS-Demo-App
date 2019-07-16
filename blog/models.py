from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=75)
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    def summary(self):
        return self.text[:75] + '...'

#returns the title instead of a none decriptive name when looking in the admin section eg database
    def __str__(self):
        return self.title
