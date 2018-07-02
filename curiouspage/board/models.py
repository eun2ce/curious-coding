from django.db import models
#db
# Create your models here.
#https://blog.hannal.com/2008/6/04_2-python_django_lecture/ 출처
class Board (models.Model):
    title=models.CharField(max_length=80,null=False) #글제목
    content=models.TextField(null=False)    #글내용
    created = models.DateTimeField(auto_now_add=True) #글생성
    updated = models.DateTimeField(auto_now=True)   #글수정
    # tags=models.ManyToManyField(TagModel) #꼬리표 // 글 갈래
    # category =models.ForeignKey(categories) #카테고리
    comments = models.PositiveSmallIntegerField(default=0,null=True) # 댓글 수 // 양수만
    # 각 필드 문자를 반환하는 함수

    def __strTitle__(self):
        return self.title
    def __strText__(self): 
        return self.content
    def __strcreated__(self):
        return self.created
    def __strupdated__(self):
        return self.updated
    def __strcomments__(self):
        return self.comments
    # def was_published_recently(self):   사용법 아직 모름
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class BoardTitle (models.Model):
    title=models.ForeignKey(Board,on_delete=models.CASCADE)


    """
    from django.db import models
#db
# Create your models here.
#https://blog.hannal.com/2008/6/04_2-python_django_lecture/ 출처
class BoardTitle (models.model):
    title=models.CharField(max_length=80,null=False)

class Board (models.Model):
    title=models.ForeignKey(BoardTitle,on_delete=models.CASCADE) #글제목
    content=models.TextField(null=False)    #글내용
    created = models.DateTimeField(auto_now_add=True) #글생성
    updated = models.DateTimeField(auto_now=True)   #글수정
    # tags=models.ManyToManyField(TagModel) #꼬리표 // 글 갈래
    # category =models.ForeignKey(categories) #카테고리
    comments = models.PositiveSmallIntegerField(default=0,null=True) # 댓글 수 // 양수만
    # 각 필드 문자를 반환하는 함수

    def __strTitle__(self):
        return self.title
    def __strText__(self): 
        return self.content
    def __strcreated__(self):
        return self.created
    def __strupdated__(self):
        return self.updated
    def __strcomments__(self):
        return self.comments
    # def was_published_recently(self):   사용법 아직 모름
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    """