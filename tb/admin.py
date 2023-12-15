from django.contrib.admin import ModelAdmin as MA, register
from tb.models import TelegramUser
from tb.forms import TelegramUserForm

@register(TelegramUser)
class TelegramUserAdmin(MA):
    list_display = ('id', 'external_id', 'name', 'is_admin')
    form = TelegramUserForm