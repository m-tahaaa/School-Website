from django.urls import path

from . import views


app_name = "school"

urlpatterns = [
    path("", views.home, name="home"),
    path("admission/", views.admission, name="admission"),
    path("notices/", views.notices, name="notices"),
    path("prospectus/", views.prospectus, name="prospectus"),
]
