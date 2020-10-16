from django.contrib import admin
from .models import Categories, Materials, Colors, Sizes, Products, Portfolio, Subscribe, Team, Review


class CategoriesConfig(admin.ModelAdmin):
    fields = ('name', 'icon', 'slug_category')
    prepopulated_fields = {'slug_category': ('name',)}
    list_display = fields


admin.site.register(Categories, CategoriesConfig)


class MaterialsConfig(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields


admin.site.register(Materials, MaterialsConfig)


class ColorsConfig(admin.ModelAdmin):
    fields = ('name', 'color')
    list_display = fields


admin.site.register(Colors, ColorsConfig)


class SizesConfig(admin.ModelAdmin):
    fields = ('name',)
    list_display = fields


admin.site.register(Sizes, SizesConfig)


class ProductsConfig(admin.ModelAdmin):
    fields = (
        'name',
        'slug_product',
        'brand',
        ('category', 'availability', 'new', 'popularity'),
        ('price', 'price_discount', 'discount'),
        'materials',
        'colors',
        'sizes',
        'img1',
        'img2',
        'img3',
        'img4',
        'img5'
    )
    list_display = ('name', 'category', 'price', 'popularity')
    prepopulated_fields = {'slug_product': ('name',)}


admin.site.register(Products, ProductsConfig)


class PortfolioConfig(admin.ModelAdmin):
    fields = ('name', 'url', 'img')
    list_display = ('name', 'url', 'img')


admin.site.register(Portfolio, PortfolioConfig)


class SubscribeConfig(admin.ModelAdmin):
    fields = ('mail',)
    list_display = ('mail', 'date')


admin.site.register(Subscribe, SubscribeConfig)


class TeamConfig(admin.ModelAdmin):
    fields = ('name',
              'img',
              'status',
              'phone',
              'instagram',
              'mail')
    list_display = ('name', 'img', 'status')
    admin.site.register(Team)


class ReviewConfig(admin.ModelAdmin):
    fields = ('name',
              'img',
              'description',
              )
    list_display = ('name', 'img', 'description')
    admin.site.register(Review)

