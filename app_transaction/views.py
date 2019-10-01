from django.shortcuts import render
from django.db import transaction

from .models import Group

# Create your views here.

def save_with_exception(request):
    g1=Group()
    g1.name='save with exception'
    g1.save()

    raise Exception("Error")
    #obj is not stored to db

def save_without_exception(request):
    g1=Group()
    g1.name='save without exception'
    g1.save()
    #obj is stored to db

@transaction.non_atomic_requests
def non_atomic(request):
    g1=Group()
    g1.name='non atomic request'
    g1.save()

    raise Exception("Error")
    #obj is stored to db

def save_outside():
    g1=Group()
    g1.name='save outside'
    g1.save()

def outside(request):
    save_outside()
    raise Exception("Error")
    #obj is not stored to db

def exception_in_try_except_block(request):
    try:
        g1=Group()
        g1.name='exception in try except block'
        g1.save()

        raise Exception("Error")
    except:
        pass

    #obj is stored to db

def outer_inner_1(request):
    g1=Group()
    g1.name='outer transaction no exception 1'
    g1.save()

    try:
        with transaction.atomic(): # context manager
            g2=Group()
            g2.name='inner transaction with exception 1'
            g2.save()
            raise Exception("Error")
    except:
        pass

def outer_inner_2(request):
    g1=Group()
    g1.name='outer transaction no exception 2'
    g1.save()

    try:
        with transaction.atomic(): # context manager
            g2=Group()
            g2.name='inner transaction with exception 2'
            g2.save()

        raise Exception("Error")
    except:
        pass

def atomic_1(resquest):
    g1=Group()
    g1.name="atomic_1 save 1"
    g1.save()

    with transaction.atomic():
        g2=Group()
        g2.name="atomic_1 save 2"
        g2.save()

    g3=Group()
    g3.name="atomic_1 save 3"
    g3.save()

@transaction.atomic
def atomic_2(resquest):
    g1=Group()
    g1.name="atomic_2 save 1"
    g1.save()

    with transaction.atomic():
        g2=Group()
        g2.name="atomic_2 save 2"
        g2.save()

    g3=Group()
    g3.name="atomic_2 save 3"
    g3.save()

def atomic_3(resquest):
    g1=Group()
    g1.name="atomic_3 save 1"
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            g2.name="atomic_3 save 2"
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

    g3=Group()
    g3.name="atomic_3 save 3"
    g3.save()

@transaction.atomic
def atomic_4(resquest):
    g1=Group()
    g1.name="atomic_4 save 1"
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            g2.name="atomic_4 save 2"
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

    g3=Group()
    g3.name="atomic_4 save 3"
    g3.save()

def atomic_5(resquest):
    g1=Group()
    g1.name="atomic_5 save 1"
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            g2.name="atomic_5 save 2"
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    g3.name="atomic_5 save 3"
    g3.save()

    raise Exception("Error 2")

@transaction.atomic
def atomic_6(resquest):
    g1=Group()
    g1.name="atomic_6 save 1"
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            g2.name="atomic_6 save 2"
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    g3.name="atomic_6 save 3"
    g3.save()

    raise Exception("Error 2")

@transaction.atomic
def atomic_7(resquest):
    g1=Group()
    g1.name="atomic_7 save 1"
    g1.save()

    with transaction.atomic():
        g2=Group()
        g2.name="atomic_7 save 2"
        g2.save()

    g3=Group()
    g3.name="atomic_7 save 3"
    g3.save()

    raise Exception("Error 2")

#@transaction.atomic
def atomic_8(resquest):
    g1=Group()
    g1.name="atomic_8 save 1"
    g1.save()

    with transaction.atomic():
        g2=Group()
        g2.name="atomic_8 save 2"
        g2.save()

    g3=Group()
    g3.name="atomic_8 save 3"
    g3.save()

    raise Exception("Error 2")

def atomic_9(resquest):
    g1=Group()
    g1.name="atomic_9 save 1"
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            g2.name="atomic_9 save 2"
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    g3.name="atomic_9 save 3"
    g3.save()
