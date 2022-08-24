from cmath import log
import re
from turtle import position

from app.serializers import BookSerializer,AccountSerializer
from .models import Book,Account
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


@api_view(('GET','POST','DELETE'))
def Logout(request,pk=None):
    logout(request)
    return Response({'message':"Logged out"})


@api_view(('GET','POST','DELETE'))
def borrow(request,pk=None):
    try:
        account=Account.objects.get(user=request.user)
        book=Book.objects.get(id=pk)
        if book.Status=="Borrowed":
            return Response({"Message":"Book Not availabe"})
        book.Owner=account
        book.Status="Borrowed"
        book.save()
        return Response({"msg":"Book Given"})
    except Book.DoesNotExist:
        return Response({"msg":"You Book Not Found"})
    except Account.DoesNotExist:
        return Response({"msg":"Login First"})




@api_view(('GET','POST'))
def addmember(request):
    if request.method=="POST":
        account=Account.objects.get(user=request.user)
        if account.position!="Librarian":
            return Response({"Message":"You can't add an Member"})
        userName = request.data['username']
        userPass = request.data['password']
        userMail = request.data['email']
        user=User.objects.create(username=userName,email=userMail,password=userPass)
        Account.objects.create(user=user,position="Member")
        return Response({"Message":"Member Added"})
    else:
        return Response({"username":"","password":"","email":""})


@api_view(('GET','POST'))
def updatemember(request,pk=None):
    account=Account.objects.get(user=request.user)
    if account.position!="Librarian":
        return Response({"Message":"You can't update an Member"})
    account=Account.objects.get(id=pk)
    account.position="Librarian"
    account.save()
    return Response({"Message":"Member Updated to Librarian"})

@api_view(('GET','POST'))
def Return(request,pk=None):
    try:
        account=Account.objects.get(user=request.user)
        book=Book.objects.get(id=pk)
        if book.Owner!=account:
            return Response({"Message":"Please send the owner to return"})
        book.Owner=None
        book.Status="Available"
        book.save()
        return Response({"msg":"Book Return"})
    except Book.DoesNotExist:
        return Response({"msg":"You Book Not Found"})
    except Account.DoesNotExist:
        return Response({"msg":"Login First"})



@api_view(('GET','POST','DELETE'))
def View(request,pk=None):
    try:
        book=Book.objects.get(id=pk)
        srlzr=BookSerializer(book)
        return Response(srlzr.data)
    except Book.DoesNotExist:
        return Response({"msg":"You Book Not Found"})


@api_view(('GET','POST','DELETE'))
def profileview(request,pk=None):
    try:
        ca=Account.objects.get(user=request.user)
        if ca.position!="Librarian":
            return Response({"Message":"You are not an librarian You cant see other Profile"})
        account=Account.objects.get(id=pk)
        book=Book.objects.filter(Owner=account)
        srlzr=BookSerializer(book,many=True)
        return Response(srlzr.data)
    except Book.DoesNotExist:
        return Response({"msg":"You Book Not Found"})






@api_view(('GET','POST'))
def available(request):
    books=Book.objects.filter(Status="Available")
    srlzr=BookSerializer(books,many=True)
    return Response(srlzr.data)







class bookActionIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        books=Book.objects.all()
        srlzr=BookSerializer(books,many=True)
        return Response(srlzr.data)

    def post(self, request,name=None):
        try:
            account=Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return Response({"msg":"You Are not an user"})
        if account.is_librarian == False:
            return Response({"Message":"You are not a Librarian"})
        Name = request.data['Name']
        book = Book.objects.create(Name=Name,Status="Available")
        return Response({"msg":"The book created sucessfully"})
    def delete(self, request,pk=None):
        try:
            account=Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return Response({"msg":"You Are not an user"})
        
        if account.is_librarian == False:
            return Response({"Message":"You are not a Librarian"})
        book = Book.objects.get(id=request.data['pk'])
        book.delete()
        return Response({"msg":"The book deleted sucessfully"})
    def put(self, request, pk=None,Name=None):
        try:
            account=Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return Response({"msg":"You Are not an user"})
        if account.is_librarian == False:
            return Response({"Message":"You are not a Librarian"})
        try:
            book=Book.objects.get(id=request.data['pk'])
            book.Name=request.data['Name']
            book.save()
            return Response({"msg":"The book updated sucessfully"})
        except Book.DoesNotExist:
            return Response({"msg":"Book Not found"})

class accountAction(APIView):
    def get(self,request):
        return Response({"username":"","password":"","email":"","position":""})
    def post(self,request):
        userName = request.data['username']
        userPass = request.data['password']
        userMail = request.data['email']
        user = User.objects.create_user(userName, userMail, userPass)
        position=request.data['position']
        Account.objects.create(user=user,position=position)
        return Response({"msg":"The User created sucessfully"})
    def delete(self, request):
        cur=Account.objects.get(user=request.user)
        print(request.data['pk'])
        account=Account.objects.get(id=request.data['pk'])
        tuser=account.user
        if cur.is_librarian == True or tuser==request.user:
            tuser.delete()
            return Response({"Message":"Account deleted"})
        return Response({"Message":"Account deleted can't be as you are Librarian and not owner of Account"})    