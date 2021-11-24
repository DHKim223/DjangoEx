from django.db import models
from member.choice import DEPARTMENT_CHOICE, GRADE_CHOICE, LEVEL_CHOICE
# Create your models here.

class Member(models.Model):
    # 아이디
    id = models.CharField(max_length=30, verbose_name="아이디", primary_key=True )
    # 비밀번호
    passwd = models.CharField(max_length=30, verbose_name="비밀번호",null=False)
    # 이름
    name = models.CharField(max_length=50, verbose_name="이름", null=False)
    # 학번
    student_id=models.CharField(max_length=10,verbose_name="학번",null=False)
    # 학과
    department = models.CharField(choices=DEPARTMENT_CHOICE, max_length=50, verbose_name="학과", null=False)
    # 학년    /    졸업생
    grade=models.CharField(choices=GRADE_CHOICE, max_length=20,verbose_name="학년", null=False)
    # 사용자 권한
    level=models.CharField(choices=LEVEL_CHOICE,max_length=30, verbose_name="등급", null=False)
    # 가입일
    join_date=models.DateTimeField(auto_now_add=True, verbose_name="가입일",null=False,blank=True)
    
    
    
    