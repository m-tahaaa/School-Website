from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import AdmissionApplicationForm
from .models import Event, GalleryPhoto, Notice


def home(request):
    context = {
        "notices": Notice.objects.all()[:4],
        "gallery_photos": GalleryPhoto.objects.all()[:6],
        "events": Event.objects.filter(event_date__gte=request_today())[:3],
    }
    return render(request, "index.html", context)


def prospectus(request):
    return render(request, "prospectus.html")


def request_today():
    from django.utils.timezone import localdate

    return localdate()


def admission(request):
    if request.method == "POST":
        form = AdmissionApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been received. Our admissions team will contact you shortly.")
            return redirect("school:admission")
    else:
        form = AdmissionApplicationForm()
    return render(request, "admission.html", {"form": form})


def notices(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    notice_list = Notice.objects.all()
    if query:
        notice_list = notice_list.filter(title__icontains=query) | notice_list.filter(content__icontains=query)
    if category:
        notice_list = notice_list.filter(category=category)
    context = {"notices": notice_list, "query": query, "selected_category": category}
    template = "partials/notice_list.html" if request.headers.get("HX-Request") else "notices.html"
    return render(request, template, context)
