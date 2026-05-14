from django.contrib import admin
from .models import Player, PlayerStats


class PlayerStatsInline(admin.TabularInline):
    model = PlayerStats
    extra = 1


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'role')
    inlines = [PlayerStatsInline]


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerStats)