from django.contrib import admin

# Register your models here.
from .models import Board,Category

#localhost:8000/admin/ 에서 db 내용 건드릴 수 있도록
admin.site.register(Board)
admin.site.register(Category)