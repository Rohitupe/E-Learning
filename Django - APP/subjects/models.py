from django.db import models

# Create your models here.
class Subject(models.Model):
    bookName = models.CharField(max_length = 200)
    bookDescription = models.TextField()
    bookImage = models.ImageField(upload_to='subjects/images')
    bookPro = models.BooleanField(verbose_name="Pro Subjects",default=False)

    def __str__(self):
        return self.bookName


class SubjectVideo(models.Model):
    bookName = models.ForeignKey(Subject, on_delete=models.CASCADE)
    videoFiles = models.FileField(upload_to="subjects/Videos", null=True, blank=True)
    pdfFile = models.FileField(upload_to="subjects/pdfFiles", null=True, blank=True)

    def __str__(self):
        return f"{str(self.bookName)},{str(self.id)}"
    
