
from django.db import models
from hashlib import md5

class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash_value = models.CharField(max_length=16)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_url

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        self.url_hash_value = md5(self.full_url.encode()).hexdigest()[:10]
        return super().save(*args, **kwargs)


class URL_hash(models.Model):
    date_use = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=155)
    if_mobile = models.BooleanField()
    url = models.ForeignKey(URL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_agent



