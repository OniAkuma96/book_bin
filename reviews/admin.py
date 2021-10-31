from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'date'
    )

admin.site.register(Review, ReviewAdmin)
