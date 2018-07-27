from django.contrib import admin
from .models import Event, Product, AmazingQuotesAbout, TeamMember, Value, Order,Quote


# Register your models here.


class ValuesInLine(admin.TabularInline):
    model = Value
    extra = 3


class AmazingQuotesAboutAdmin(admin.ModelAdmin):
    inlines = [ValuesInLine]


class OrderInLine(admin.TabularInline):
    model = Order
    extra = 10


class ProductAdmin(admin.ModelAdmin):
    inlines = [OrderInLine]


class QuoteAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_of_publish"]


admin.site.register(Event)
admin.site.register(Product, ProductAdmin)
admin.site.register(AmazingQuotesAbout, AmazingQuotesAboutAdmin)
admin.site.register(TeamMember)
admin.site.register(Quote,QuoteAdmin)
