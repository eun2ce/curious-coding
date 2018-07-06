from django.db import models
#db
# Create your models here.
#https://blog.hannal.com/2008/6/04_2-python_django_lecture/ 출처
class Board (models.Model):
    title=models.CharField(max_length=80,null=False) #글제목
    content=models.TextField(null=False)    #글내용
    file=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/') # 파일
    created = models.DateTimeField(auto_now_add=True) #글생성
    updated = models.DateTimeField(auto_now=True)   #글수정
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    title = models.ForeignKey(Board,on_delete=models.CASCADE)
    author =models.CharField(max_length = 10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title