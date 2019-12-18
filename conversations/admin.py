from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation Admin Definition"""

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )


# Register your models here.
@admin.register(models.Message)
class MessagenAdmin(admin.ModelAdmin):
    """Message Admin Definition"""

    list_display = (
        "__str__",
        "created",
    )

