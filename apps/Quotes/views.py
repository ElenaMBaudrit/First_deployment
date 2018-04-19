from django.shortcuts import render,redirect
from django.contrib import messages
from models import *
import bcrypt
# Create your views here.

def index(request):

    return render (request,'Quotes/index.html')

def register(request):
    result = User.objects.valid_reg(request.POST)
    if result[0]:
        request.session['user_id'] = result[1].id
        request.session['name'] = result[1].name
        return redirect('/Quotes/dashboard')
    else:
        for error in result[1]: 
            messages.add_message(request, messages.INFO, error)
        return redirect(request, '/')

def new_user(request):
    return redirect('/Quotes/dashboard')
def login(request):
    result = User.objects.validate_log(request.POST)
    if result[0]:
        request.session['user_id'] = result[1].id
        request.session['email'] = result[1].name
        return redirect('/Quotes/dashboard')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def posts(request):
    return render(request, 'Quotes/posts.html')

def create_post(request):
    result = Quote.objects.validate_quote(request.POST)
    if result[0]:
        request.session['quote_id'] = result[1].id
        request.session['author'] = result[1].author
        request.session['description'] = result[1].description
        request.session['creator'] = User.objects.get(id=request.session['user_id'])
        return redirect('/Quotes/dashboard')

    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect ('/Quotes/dashboard')


def add_to_list(request, user_id):
    this_user =  User.objects.get(id=requeest.session['user_id'])
    this_quote = Quote.objects.get(id=quote_id)
    this_quote.others.add(this_user)
    return redirect('/Quotes/dashboard')

def remove_from_list(request):
    pass

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'my_quotes': user.added_by.all(),
        'others_quotes': Quote.objects.exclude(creator = user),
        'not_my_quote': Quote.objects.exclude(others__name = request.session['name']).all()
    }
    return render(request, 'Quotes/dashboard.html', context)


