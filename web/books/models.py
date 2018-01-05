from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
 
    def __str__(self):
        return self.firstname + " " + self.lastname

class Books(models.Model):
    book_title = models.CharField(max_length=100, blank=False)
    # book_photo = models.FileField()
    writer = models.CharField(max_length=50, blank=False)
    synopsis = models.CharField(max_length=200, blank=True)
    publisher = models.CharField(max_length=50)
    publish_date = models.DateField()

    def __str__(self):
        return self.book_title+" "+self.writer