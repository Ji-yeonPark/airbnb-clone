from django.utils import timezone
from django.urls import reverse
from django.views.generic import ListView, View
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django_countries import countries
from . import models, forms

# Create your views here.
class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    """RoomDetail Definition"""

    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}
                if city != "Anywhere":
                    filter_args["city__startswith"] = city
                filter_args["country"] = country
                if room_type is not None:
                    filter_args["room_type"] = room_type
                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms
                if beds is not None:
                    filter_args["beds__gte"] = beds
                if baths is not None:
                    filter_args["baths__gte"] = baths
                if instant_book is True:
                    filter_args["instant_book"] = True
                if superhost is True:
                    filter_args["host__superhost"] = True
                rooms = models.Room.objects.filter(**filter_args)
                for amenity in amenities:
                    rooms = rooms & models.Room.objects.filter(amenities__pk=amenity.pk)
                for facility in facilities:
                    rooms = rooms & models.Room.objects.filter(
                        facilities__pk=facility.pk
                    )

                paginator = Paginator(rooms, 3)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)

                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms},
                )
        else:
            form = forms.SearchForm()
        return render(request, "rooms/search.html", {"form": form})
