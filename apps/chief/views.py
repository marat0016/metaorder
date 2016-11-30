from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect
from django.utils import timezone
from metaord.utils.decorators import group_required


login_url = '/login/'

@group_required('chief', login_url=login_url)
def index(request):
    return render(request, 'chief/index.html', {})
