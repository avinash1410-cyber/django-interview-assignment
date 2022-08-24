from django.urls import path

from .views import *
urlpatterns=[
    path('available/',available),
    path('bookborrow/<int:pk>/',borrow),
    path('bookreturn/<int:pk>/',Return),
    path('bookView/<int:pk>/',View),
    path('profileView/<int:pk>/',profileview),
    path('book/',bookActionIView.as_view()),
    path('account/',accountAction.as_view()),
    path('addmember/',addmember),
    path('updatemember/<int:pk>/',updatemember),
]