from django.db import models


# Create your models here.

class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.CharField( max_length=80)
    skillIcon = models.ImageField(upload_to='static/img/skills')
    progress = models.IntegerField()

    def __str__(self):
        return self.skill

class About(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    fend = models.CharField(max_length=300,null=True)
    bend = models.CharField(max_length=300,null=True)
    db = models.CharField(max_length=300,null=True)
    pl = models.CharField(max_length=300,null=True)
    tools = models.CharField(max_length=300, null=True)
    software = models.CharField(max_length=300)

    def __str__(self):
        return self.fend

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    shortDes = models.CharField(max_length=500)
    content = models.TextField()
    category = models.CharField(max_length=30)
    skills = models.CharField(max_length=200)
    feature = models.ImageField(upload_to="static/img/projects")
    pimg1 = models.ImageField(upload_to="static/img/projects")
    pimg2 = models.ImageField(upload_to="static/img/projects")
    pimg3 = models.ImageField(upload_to="static/img/projects")
    live = models.CharField(max_length=300, null=True, default="")
    code = models.CharField(max_length=300)


    def __str__(self):
        return self.name
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    msg = models.TextField()

    def __str__(self):
        return self.name
    