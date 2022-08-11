from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):

    return render_to_response('index.html', locals())

