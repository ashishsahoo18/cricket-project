from django.contrib import admin
from .models import Player, PlayerStats


# Player Stats Inline
class PlayerStatsInline(admin.TabularInline):

    model = PlayerStats

    extra = 0

    max_num = 4


# Player Admin
class PlayerAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'country',
        'role'
    )

    search_fields = (
        'name',
        'country',
        'role'
    )

    list_filter = (
        'country',
        'role'
    )

    inlines = [PlayerStatsInline]


# Player Stats Admin
class PlayerStatsAdmin(admin.ModelAdmin):

    list_display = (
        'player',
        'format',
        'matches',
        'runs',
        'wickets'
    )

    list_filter = (
        'format',
    )

    search_fields = (
        'player__name',
    )


# Register Models
admin.site.register(Player, PlayerAdmin)

admin.site.register(PlayerStats, PlayerStatsAdmin)