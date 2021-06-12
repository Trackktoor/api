from django.db import models

def get_default_from_photos():
    return {'SmallMobile ': '', 'StoryMobile': '', 'MockupMobile': '', 'BigDesktop': '', 'MockupDesktop': ''}

class project(models.Model):
    name = models.CharField(max_length=155)
    project_type = models.IntegerField()
    short_task = models.CharField(max_length=155)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    project_link = models.CharField(max_length=255)
    photos = models.JSONField()

    def __str__(self):
        return self.name

class new_project_request(models.Model):
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=55)
    email = models.EmailField(blank=True)
    comment = models.TextField(blank=True)
    project_type = models.CharField(blank=True, max_length=155)
    project_theme = models.CharField(blank=True, max_length=255)
    status = models.CharField(blank=True, max_length=55)

class new_consult_request(models.Model):
    phone = models.CharField(max_length=55)
    comment = models.TextField(blank=True)
