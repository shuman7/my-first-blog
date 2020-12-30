##from とか import で始まる行は全部、他のファイルから何かをちょこっとずつ追加する行です
from django.conf import settings 
from django.db import models
from django.utils import timezone


class Post(models.Model): ##今回のPostモデル定義
    ##プロパティ定義
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): ##ブログを公開するメソッドそのもの defはファンクション（関数）/メソッドという意味
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title