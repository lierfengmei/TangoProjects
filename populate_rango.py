#!/usr/bin/env python
# encoding: utf-8

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'TangoProject.settings')

import django
django.setup()
from rango.models import Category,Page


def populate():

    python_pages=[
        {"title":"Official Python Tutorial","url":"http://docs.python.org/2/tutorial/","views":25},
        {"title":"How to Think like a Computer Scientist","url":"http://www.greenteapress.com/thinkpython/","views":88},
        {"title":"Lear Python in 10 minutes","url":"http://www.korokithakis.net/tutorials/python/","views":72}
        ]

    django_pages=[
        {"title":"Official Django Tutorial","url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01/","views":34},
        {"title":"Django Rocks","url":"http://www.djangorocks.com/","views":10},
        {"title":"How to Tango with Django","url":"http://www.tangowithdjango.com/","views":345}
    ]

    other_pages=[
        {"title":"Bottle","url":"http://bottlepy.org/docs/dev/","views":87},
        {"title":"Flask","url":"http://flask.pocoo.org","views":5}
    ]

    # Create a dictionary of dictionaries for our categories.
    cats = {"Python":{"pages":python_pages,"views":128,"likes":64},
            "Django":{"pages":django_pages,"views":64,"likes":32},
            "Other Frameworks":{"pages":other_pages,"views":32,"likes":16}
    }

    # The code below goes through the cats dictionary, then add each Category,
    # add then adds all the associated pages for the category.

    for cat,cat_data in cats.items(): # for key value in dic.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])              # cat is "Python" "Django" "Other Frameworks"
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0}-{1}".format(str(c),str(p)))



def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category = cat,title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

#Start execution here!
if __name__=='__main__':
    print("Starting Rango population script...")
    populate()


