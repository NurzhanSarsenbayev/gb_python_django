from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.action(description='Reset quantity')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.action(description='Set price to 100')
def set_price(modeladmin, request, queryset):
    queryset.update(price=100)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category','-quantity']
    list_filter = ['date_added','price']
    search_fields = ['description']
    search_help_text = 'Search by description'
    actions = [reset_quantity, set_price]

    """Single product"""

    #fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields':['name'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],
                'description': 'Product category and its advanced options',
                'fields':['category','description'],
            },
        ),
        (
            'Accounting',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Rating and date',
            {
                'description':'Rating is based on customer feedback',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
