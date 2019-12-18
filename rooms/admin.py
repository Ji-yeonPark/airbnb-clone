from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules",),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name",)

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    search_fields = ("^city", "^host__username")
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        """
        self: 부모 클래스
        object: 현재 행(row)
        """
        # print(obj.amenities.all()) -> QuerySet
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    # 필드 명 변경 (변경하면 자동 정렬 안됨.)
    # count_amenities.short_description = "amenity"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
