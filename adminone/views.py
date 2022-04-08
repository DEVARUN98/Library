from django.shortcuts import render,redirect
from adminone.forms import BookForm,LoginForm
from adminone.forms import SignupForm
from django.contrib.auth import logout
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from adminone.models import Book
from django.urls import reverse_lazy

def home(request):
    return render(request,"home.html")

class BookAddView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "bookAdd.html"
    success_url =reverse_lazy("retrieve")

class BookRetrieveView(ListView):
    model = Book
    template_name = "bookList.html"
    context_object_name = "books"

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    pk_url_kwarg = "id"      #to uniquely select one book using ID
    template_name = "bookUpdate.html"
    success_url = reverse_lazy("retrieve")   # after success, it returns to the "retrieve " page

class BookDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = "id"
    template_name = "bookDelete.html"
    success_url = reverse_lazy("retrieve")

class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignupForm     # To specify the form needed for the html file to write
    success_url = reverse_lazy('login')

class LoginView(CreateView):
    template_name = "login.html"
    success_url = reverse_lazy('home')
    form_class = LoginForm


def sign_out(request):
    logout(request)
    return redirect("signin")
# Create your views here.
