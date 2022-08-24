from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET','POST'))
def Home(request):
    dictionary={
        "path('available/',available),--->Will Show all the available Books",
        "path('bookborrow/<int:pk>/',borrow),--->For borrow a particular Book pk is the id of that book",
        "path('bookreturn/<int:pk>/',Return),---->For Return a particular Book pk is the id of that book after return Book Will availbe again",
        "path('bookView/<int:pk>/',View),---->show the book status,owner,",
        "path('profileView/<int:pk>/',profileview),--->Profile view of a Member ",
        "path('book/',bookActionIView.as_view()),---->Book class which take action on followinf request",
		"get--->show all books",
		"post--->for create a books by posting the books name",
		"delete-->for delete a book by sending the id(pk) of book",
		"put--->Update the name of book by sending the name and id(pk) of the book ",
        "path('account/',accountAction.as_view())",
		"get--->show credential for create a account",
		"post--->for create a memeber in system",
		"delete-->librarain or owner of that account can delete a account",
        "path('addmember/',addmember),-->libraraina can add a new mener in system",
        "path('updatemember/<int:pk>/',updatemember),----->libraraina can update a new status from member to libraraian of a member",
        "path('admin/', admin.site.urls),--->admin for project",
        "path('app/', include('app.urls')),---->append app before above all requests",
        "path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),---->generate token for a user by username and passowrd",
        "path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),-->referhs token",
        "path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),---->verify token",
    }
    return Response(dictionary)