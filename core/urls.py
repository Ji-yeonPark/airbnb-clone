from django.urls import path
from rooms import views as room_view

_name = "core"
urlpatterns = [path("", room_view.all_rooms, name="home")]
