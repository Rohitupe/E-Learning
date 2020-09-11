from django.db import models

# Create your models here.

class ClassName(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class ClassSubject(models.Model):
    class_name = models.ForeignKey(ClassName,on_delete=models.CASCADE, related_name='cSub')
    class_subject = models.CharField(max_length=100)

    def __str__(self):
        return str(self.class_name) + " " + self.class_subject

class ClassTopic(models.Model):
    class_subject = models.ForeignKey(ClassSubject,on_delete=models.CASCADE, related_name='cTop')
    chapter_name = models.CharField(max_length=150)
    chapter_topic = models.TextField()

    def __str__(self):
        return str(self.class_subject) + " " +self.chapter_name
