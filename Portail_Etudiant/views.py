from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import CodeInkForm
from .models import Uuser
from .models import cours
from .models import Lesson
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from youtubesearchpython import VideosSearch

@csrf_protect

# Create your views here.

# def base(request):
#     return render(request,'Portail_Etudiant/base.html')

def registre(request):
    name = request.session.get('name', '')
    email = request.session.get('email', '')
    surname = request.session.get('surname', '')

    return render(request, 'inscription.html', {'name':name, 'email':email,'surname':surname})
    
def thanks(request):
    return render(request, 'thank-you.html')

def sub1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('username')
        passw = request.POST.get('pass')
        passw_conf = request.POST.get('passconf')

        if User.objects.filter(username=name).exists():
                messages.error(request,'This username is already taken. Please enter a new one. ')
                return redirect ('/registre/')
        if User.objects.filter(email=email).exists():
                messages.error(request,'This email already exists. Please enter a new one.')
                return redirect ('/registre/')
        
        if passw != passw_conf:
        # Enregistrez les données du formulaire dans les variables de session
            request.session['name'] = name
            request.session['surname'] = surname
            request.session['email'] = email

            return redirect ('/registre/')
        else:
            form = User.objects.create_user(username=name,email=email,password=passw,first_name=name,last_name=surname)
            form.save()
            return redirect('/thanks/')

def login(request):
    email = request.session.get('email', '')
    return render(request, 'login.html', {'email':email})

def sub2(request):
     if request.method == 'POST':
        email = request.POST.get('username')
        passw = request.POST.get('pass')
        request.session['email'] = email
        try:
            a=User.objects.get(email=email).username
            print(a)
        except:
            messages.error(request,"Cet utilisateur n'existe pas dans la base")
            return redirect('/login/')
        user = authenticate(request, username=a, password=passw)
        print(user)
        if (user is not None):
            dj_login(request, user)
            request.session['name'] = user.last_name 
            request.session['surname'] = user.first_name
            first_name = user.first_name
            last_name = user.last_name
            lescours = cours.objects.all()
            return redirect('/')
        else:
             messages.error(request,"Cet utilisateur n'existe pas dans la base")
             return redirect('/login/')
        
def base(request):
    if (request.user.is_authenticated):
        user=request.user
        first_name = user.first_name
        last_name = user.last_name
    lescours = cours.objects.all()
    return render(request,'base.html', locals())

def lessons(request,val):

    lescours = cours.objects.get(id=val)
    lessons = lescours.lesson_set.all()
    user=request.user
    dj_login(request, user)
    first_name = user.first_name
    last_name = user.last_name
    request.session['first_name'] = first_name
    request.session['last_name'] = last_name
    return render(request,'lesson.html', locals()) 

def logout_view(request):
    logout(request)
    return redirect('base')

def ytb(request):
    if request.method == 'POST':
        text = request.POST.get('ytbesearch')
        print(text)
        video = VideosSearch(text,limit=10) 
        result_list=[] 
        for i in video.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc =''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description']= desc
            result_list.append(result_dict)
            results = result_list
    return render(request, "youtube.html", locals())
    

def profile(request):
    name = request.session.get('name','')
    surname = request.session.get('surname','')
    return render(request,'profile.html', locals())



def profilesumitted(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        passw = request.POST.get('pass')
        passw_conf = request.POST.get('passconf')

        if passw != passw_conf:
        # Enregistrez les données du formulaire dans les variables de session
            request.session['name'] = name
            request.session['surname'] = surname
            messages.error(request,'Passwords don\'t match')
            return redirect ('/profile/')
        else:
            c=request.session['email']
            print(c)
            userr= User.objects.get(email=c)
            print(userr)
            userr.first_name=name
            userr.last_name=surname
            userr.set_password(passw)
            userr.save()
            return render(request,'thank-you.html', locals())

