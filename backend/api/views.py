from django.http import HttpResponse
from django.shortcuts import  render
from .models import User
from django.http import Http404


def index(request):
    all_Users = User.objects.all()
   # template = loader.get_template('login.html')

    context = {
        'all_Users' : all_Users,
    }
   # html = ''
    #for user in all_Users:
     #   url = '/api/' + str(User.id) + '/'
      #  html += '<a href="'+ url +'">'+ user.name+'</a><br>'
    #return HttpResponse(html)
    #return HttpResponse(template.render(context, request))
    return render(request, 'home.html', context)

def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("user does not exist")
    return render(request, 'detail.html', {'user': user})