from django.urls import path

from adminone import views


urlpatterns=[
    path("",views.home,name="home"),
    path("add/",views.BookAddView.as_view(),name="add"),
    path("delete/<int:id>",views.BookDeleteView.as_view(),name="delete"),
    path("update/<int:id>",views.BookUpdateView.as_view(),name="update"),
    path("retrieve/",views.BookRetrieveView.as_view(),name="retrieve"),
    path("logout", views.sign_out, name="signout"),

]