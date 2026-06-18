from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login ,logout
from django.shortcuts import render, redirect
from .models import Document,SearchHistory
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Document, SearchHistory
from django.shortcuts import get_object_or_404

def home(request):

    query = request.GET.get('q', '')

    results = []
    page_obj = None

    if query:

        q_object = Q()

        words = query.split()

        for word in words:

            q_object |= Q(title__icontains=word)
            q_object |= Q(content__icontains=word)

        results = Document.objects.filter(q_object)

        results = sorted(
            results,
            key=lambda doc: doc.content.lower().count(query.lower()),
            reverse=True
        )

        paginator = Paginator(results, 3)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        if request.user.is_authenticated:

            SearchHistory.objects.create(
                user=request.user,
                query=query
            )

    return render(
        request,
        'home.html',
        {
            'page_obj': page_obj,
            'query': query,
            'results': results
        }
    )
def register(request):
        if request.method=="POST":
             form=UserCreationForm(request.POST)
             if form.is_valid():
                  form.save()
                  return redirect("home")     
        else:
             form=UserCreationForm()
        return render(request,"register.html",{"form":form})
def user_login(request):
    if request.method=="POST":  
          form=AuthenticationForm(data=request.POST)
          if form.is_valid():
               user=form.get_user()
               login(request,user)
               return redirect('home')
    else:
         form=AuthenticationForm()
         return render(request,'login.html',{"form":form})
def user_logout(request):
     logout(request)
     return redirect("home")    
def history(request):
     searches=SearchHistory.objects.filter(user=request.user).order_by("-searched_at")
     return render(request,"history.html",{"searches":searches})
def delete_history(request,id):
    SearchHistory.objects.filter(
        id=id,
        user=request.user
    ).delete()

    return redirect('history')
def document_detail(request, id):

    document = get_object_or_404(
        Document,
        id=id
    )

    return render(
        request,
        'document_detail.html',
        {'document': document}
    )