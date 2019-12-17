from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation Admin Definition"""

    pass


# Register your models here.
@admin.register(models.Message)
class MessagenAdmin(admin.ModelAdmin):
    """Message Admin Definition"""

    pass

