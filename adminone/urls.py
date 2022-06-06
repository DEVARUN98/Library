
from adminone import views
from django.urls import path

urlpatterns=[
    path("home",views.home,name="home"),
    path("uhome", views.uhome, name="uhome"),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("signin",views.LoginView.as_view(),name="signin"),
    path("add/",views.BookAddView.as_view(),name="add"),
    path("delete/<int:id>",views.BookDeleteView.as_view(),name="delete"),
    path("update/<int:id>",views.BookUpdateView.as_view(),name="update"),
    path("retrieve/",views.BookRetrieveView.as_view(),name="retrieve"),
    path("logout/", views.sign_out, name="signout"),
]