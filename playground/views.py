from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, Order, Customer, Collection, OrderItem
from django.db import transaction
from django.db import connection


def say_hello(request):



    return render(request, "hello.html", {"name": "Amanuel"})


