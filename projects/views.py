from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from django.shortcuts import redirect
from	django.contrib.auth.decorators	import	login_required


def projects(request):
    return render(request, 'projects/projects.html')