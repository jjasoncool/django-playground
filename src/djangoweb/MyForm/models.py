from django.db import models

# Create your models here.


class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default='不願意透漏身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=50)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)  # 改True就可以預設為開啟

    def __str__(self):
        return self.message
