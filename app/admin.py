from django.contrib import admin
# Register your models here.
from .models import Account,Book
admin.site.register(Account)
admin.site.register(Book)