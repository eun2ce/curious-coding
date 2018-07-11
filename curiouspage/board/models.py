from django.db import models
from pytz import timezone
from django.conf import settings
#db
# Create your models here.
#https://blog.hannal.com/2008/6/04_2-python_django_lecture/ 출처

class Category(models.Model):   # 공지 유저글 인기글
    categoryname = models.CharField(max_length=10)

    def __unicode__(self):
        return self.categoryname

# class Subject(models.Model):    # 언어 데이터베이스 기타
#     subjectname = models.CharField(max_length=10)

#     def __unicode__(self):
#         return self.subjectname

class Board (models.Model):
    SUBJECT_TYPE_CHOICE = (('Language', 'Language'),
            ('Database', 'Database'),
            ('Etc', 'Etc'),)
    password = models.CharField(max_length=50,null=False)  #비밀번호
    author =models.CharField(max_length = 10,null=False) #작성자
    categoryname = models.ForeignKey(Category,default=True,on_delete=models.CASCADE)  #카테고리
    subject_type = models.CharField(
        'Subject Type', max_length=10, default='Etc', choices=SUBJECT_TYPE_CHOICE) #글주제
    title=models.CharField(max_length=80,null=False) #글제목
    content=models.TextField(null=False)    #글내용
    file=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/') # 파일
    count = models.PositiveIntegerField(default=0)  #조회수
    created = models.DateTimeField(auto_now_add=True) #글생성
    
    def __unicode__(self):
        return self.title

    def update_counter(self):
        self.count = self.count+1

    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created.astimezone(korean_timezone)
        
    def save(self, *args, **kwargs):
        if self.categoryname is None:  # Set default reference
            self.categoryname = Category.objects.get(id=2)
        super(Board, self).save(*args, **kwargs)

# class Comment(models.Model):
#     password = models.CharField(max_length=50,null=False)  #비밀번호
#     title = models.ForeignKey(Board,on_delete=models.CASCADE)
#     author =models.CharField(max_length = 10)   #작성자
#     message = models.TextField()    #코멘트
#     created = models.DateTimeField(auto_now_add=True)   #작성날짜
#     updated = models.DateTimeField(auto_now=True)   #업데이트날짜
    
#     def __unicode__(self):
#         return self.title