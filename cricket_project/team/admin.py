from django.contrib import admin
from .models import Player, PlayerStats


class PlayerStatsInline(admin.TabularInline):
    model = PlayerStats
    extra = 1
    readonly_fields = ('average', 'strike_rate')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'role')
    inlines = [PlayerStatsInline]


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerStats)