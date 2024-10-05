from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    num_books = models.Book.objects.all().count()
    num_book_instance = models.BookInstance.objects.all().count()
    num_book_avail = models.BookInstance.objects.filter(status__exact ='a').count()

    context = {
        'num_books' :num_books,
        'num_book_instance' : num_book_instance,
        'num_book_avail' :num_book_avail,
    }
    return render(request,'index.html',context)


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'

class BookCreate(LoginRequiredMixin,generic.CreateView):
    model = models.Book
    fields = '__all__'
    success_url = '/cataloge'
    template_name = 'create.html'

class BookDetail(generic.DetailView):
    model = models.Book
    template_name = 'detail.html'
    context_object_name = 'books'