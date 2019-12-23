from django.urls import path
from rooms import views as room_view

app_name = "core"
urlpatterns = [path("", room_view.HomeView.as_view(), name="home")]
