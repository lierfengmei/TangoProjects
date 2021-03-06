from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm


def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added in on the index page
            # Then we can direct tue user back to the index page
            return index(request)
        else:
            # The supplied form contained errors!
            # Just print them to the terminal!
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error message (if any)
    return render(request,'rango/add_category.html',{'form':form})


def add_page(request,category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request,category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form,'category':category}
    return render(request,'rango/add_page.html',context_dict)
    # I guess this 'rango/add_page.html' infers the local template file.
    # Which is in the 'template/rango/add_page.html'
    # It is nothing to do with the URL path.
    # So Be Careful!

def show_category(request,category_name_slug):
    #category_name_url store the encoded category name
    #create a context_dict which we can pass to the template engine
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all the associated pages
        # Note that filter will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Add our results list to the template context under name page
        context_dict['pages'] = pages

        # We also add the category object from the database to the context dictionary
        # We'll use this to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # we get here if we didn't find the specified category
        # Don't do anything
        context_dict['category'] = None
        context_dict['page'] = None

    # Go render the response and return it to the client
    return render(request,'rango/category.html',context_dict)



def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in decending order.
    # Retrieve the top 5 only - or all if less than 5
    # Place the list in the context_dict dictionary
    # that will be passed to the template engine

    context_dict = {}

    category_list = Category.objects.order_by('-likes')[:5]
  #  context_dict = {'categories':category_list}
    context_dict['categories'] = category_list

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    # Render the response and send it back
    return render(request,'rango/index.html',context_dict)


# def index_name(request):
 #   context_dict = {'variable_name':'Lifengmei','boldmessage':"Crunchy,creamy,cookie,candy,cupcake",}
 #   return render(request,'rango/index.html',context_dict)


def about(request):
    return render(request,'rango/about.html',)
