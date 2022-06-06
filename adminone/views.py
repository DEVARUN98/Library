from django.shortcuts import render,redirect
from adminone import forms
from django.contrib.auth import logout,login,authenticate
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,TemplateView
from adminone.models import Book
from django.urls import reverse_lazy


class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=forms.SignupForm()
        context={"form":form}
        return render(request,"signup.html",context)

    def post(self,request):
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('signin')

# class SigInView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         form=forms.LoginForm()
#         return render(request,"login.html",{"form":form})
#
#     def post(self,request):
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             email=form.cleaned_data["email"]
#             password=form.cleaned_data["password"]
#             user=authenticate(request,email=email,password=password)
#             if user:
#                 login(request,user)
#                 return redirect("uhome")
#             else:
#                 print("hello")
#                 return render(request,"signin")

class LoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=forms.LoginForm()
        context={"form":form}
        return render(request,"login.html",context)

    def post(self,request):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,email=email,password=password)
            if (user):
                login(request,user)
                # return redirect("uhome")
                return render(request,"uhome.html")
            else:
                return render(request,"uhome.html",{"form":form})


def home(request):
    return render(request,"home.html")

def uhome(request):
    return render(request,"uhome.html")

class BookAddView(CreateView):
    model = Book
    form_class = forms.BookForm
    template_name = "bookAdd.html"
    success_url =reverse_lazy("retrieve")

class BookRetrieveView(ListView):
    model = Book
    template_name = "bookList.html"
    context_object_name = "books"

class BookUpdateView(UpdateView):
    model = Book
    form_class = forms.BookForm
    pk_url_kwarg = "id"      #to uniquely select one book using ID
    template_name = "bookUpdate.html"
    success_url = reverse_lazy("retrieve")   # after success, it returns to the "retrieve " page

class BookDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = "id"
    template_name = "bookDelete.html"
    success_url = reverse_lazy("retrieve")

def sign_out(request):
    logout(request)
    return redirect("signin")
