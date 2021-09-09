from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

"""
    admin.site.register(Poll)の呼び出しによって、Djangoはオブジェクトの表示方法を「推測」し、
    adminでモデルの編集を行えるようにする。
    adminの表示や挙動を変える場合は、モデルを登録するときにオプションを指定する。
    https://djangoproject.jp/doc/ja/1.0/intro/tutorial02.html
"""