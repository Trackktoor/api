
from django.db import models
from hashlib import md5

class URL(models.Model):
    url = models.URLField(unique=True)
    short_url = models.CharField(max_length=16)
    redirects = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self._url

    def clicked(self):
        self.redirects += 1
        self.save()

    def save(self, *args, **kwargs):
        self.short_url = md5(self.url.encode()).hexdigest()[:5]
        return super().save(*args, **kwargs)
    def get_info(self):
        return {
            "url": self.url,
            "short_url": self.short_url,
            "redirects": self.redirects,
            "created_at": self.created_at,
            "id": self.id
        }


class URL_hash(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=155)
    if_mobile = models.BooleanField()
    ip = models.CharField(max_length=40, default=0)
    url = models.ForeignKey(URL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_agent

    def get_info(self):
        return {
            "time": self.time,
            "user_agent": self.user_agent,
            "id": self.url.id,
            "ip": self.ip,
        }



