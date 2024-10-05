from django.db import models
from django.urls import reverse

# Create your models here.

class General(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
#----------------

class Language(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
#----------------

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL,null=True)
    summary = models.TextField()
    isbin = models.CharField('ISBIN',max_length=50,unique=True)
    general = models.ManyToManyField(General)
    language = models.ForeignKey(Language,on_delete=models.SET_NULL,null=True)
    img = models.ImageField(upload_to='books/')
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={'pk':self.pk})
#----------------

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True,null=True)
    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse('author_detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return f"{self.last_name} - {self.first_name}"
    
#----------------

import uuid 

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey(Book,on_delete=models.RESTRICT)
    inprint = models.CharField(max_length=1000)
    due_back = models.DateField(null=True,blank=True)

    loan_status = (
        ('m','Maintence'),
        ('o','On loan'),
        ('a','Availabe'),
        ('r','Reserved'),
    )
    status = models.CharField(max_length=20,choices=loan_status,default='m')
    class Meta:
        ordering = ['due_back']

    def __str__(self) -> str:
        return f"{self.id} - {self.book.title}"