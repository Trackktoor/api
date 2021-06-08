from django.db import models

def get_default_from_photos():
    return {'SmallMobile ': '', 'StoryMobile': '', 'MockupMobile': '', 'BigDesktop': '', 'MockupDesktop': ''}

class Project(models.Model):
    Name = models.CharField(max_length=155)
    TaskType = models.CharField(max_length=155)
    ProjectType = models.IntegerField()
    ShortTask = models.CharField(max_length=155)
    CreateDate = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    ProjectLink = models.CharField(max_length=255)
    Photos = models.JSONField()

    def __str__(self):
        return self.Name

class NewProjectRequest(models.Model):
    Name = models.CharField(max_length=155)
    Phone = models.CharField(max_length=55)
    Email = models.EmailField()
    Comment = models.TextField()
    ProjectType = models.IntegerField()
    ProjectTheme = models.CharField(max_length=255)
    ProjectStatus = models.CharField(max_length=55)

class NewConsultRequest(models.Model):
    Phone = models.CharField(max_length=55)
    Comment = models.TextField()
