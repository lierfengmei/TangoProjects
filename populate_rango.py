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
        {"title":"Official Python Tutorial","url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist","url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Lear Python in 10 minutes","url":"http://www.korokithakis.net/tutorials/python/"}
        ]

    django_pages=[
        {"title":"Official Django Tutorial","url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks","url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django","url":"http://www.tangowithdjango.com/"}
    ]

    other_pages=[
        {"title":"Bottle","url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask","url":"http://flask.pocoo.org"}
    ]

    # Create a dictionary of dictionaries for our categories.
    cats = {"Python":{"pages":python_pages},
            "Django":{"pages":django_pages},
            "Other Frameworks":{"pages":other_pages}
    }

    # The code below goes through the cats dictionary, then add each Category,
    # add then adds all the associated pages for the category.

    for cat,cat_data in cats.items(): # for key value in dic.items():
        c = add_cat(cat)              # cat is "Python" "Django" "Other Frameworks"
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

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

#Start execution here!
if __name__=='__main__':
    print("Starting Rango population script...")
    populate()

