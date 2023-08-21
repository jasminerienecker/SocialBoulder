from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import WallSection, Route
from .forms import WallSectionForm

def room(request):
    return render(request, "bouldering/room.html")

def wall_section(request, wall_id):
    try:
        wall_section = WallSection.objects.get(pk=wall_id)
    except WallSection.DoesNotExist:
        raise Http404("This wall does not exist")

    context = {
        'wall_section' : wall_section
    }
    return render(request, "bouldering/wallsection.html", context)

def add_send(request, route_id, user_id):
    nxt = request.GET.get("next", None)
    try:
        route = Route.objects.get(pk=route_id)
        user = User.objects.get(pk=user_id)
        route.users.add(user)
        route.save()
    except Route.DoesNotExist:
        raise Http404("This route does not exist")
    return redirect(nxt)

def remove_send(request, route_id, user_id):
    nxt = request.GET.get("next", None)
    try:
        route = Route.objects.get(pk=route_id)
        user = User.objects.get(pk=user_id)
        route.users.remove(user)
        route.save()
    except Route.DoesNotExist:
        raise Http404("This route does not exist")
    return redirect(nxt)

def upload_image(request, wall_id):
    wall_section = WallSection.objects.get(pk=wall_id)

    if request.method == "POST":
        form = WallSectionForm(request.POST, request.FILES, instance=wall_section, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            form.save()
            context = {
                'wall_section' : wall_section
            }
            return render(request, "bouldering/wallsection.html", context)
        else:
            raise Http404(form.errors)
    form = WallSectionForm(instance=wall_section)
    return render(request=request, template_name="bouldering/uploadimage.html", context={"form":form})
