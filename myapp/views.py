from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import jwt

def index(request):
    j = jwt.__version__
    return render(request, 'index.html', {'user': request.user, 'j': j})
