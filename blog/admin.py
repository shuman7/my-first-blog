from django.contrib import admin
from .models import Post ##制作したPosモデルをimportしている

admin.site.register(Post)