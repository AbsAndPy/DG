from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from django.shortcuts import redirect
from	django.contrib.auth.decorators	import	login_required


def models3d(request):
    return render(request, 'models3d/models3d.html')

def wanderers_index(request):
    return render(request, 'models3d/wanderers/index.html')