from django.contrib import admin
from apps.secondary import models
# Register your models here.

# nurai's register
class StyleInfoInline(admin.TabularInline):
    model = models.StyleInfo
    extra = 1

class StyleFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [StyleInfoInline]



class GlanceFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
   


class DiscountFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
    
class CollectionInfoInline(admin.TabularInline):
    model = models.CollectionInline
    extra = 1

class CollectionFilterAdmin(admin.ModelAdmin):
    inlines = [CollectionInfoInline]


class TestimonialsInfoInline(admin.TabularInline):
    model = models.TestimonialsInline
    extra = 1

class TestimonialsFilterAdmin(admin.ModelAdmin):
    list_filter = ('mini_descriptions', )
    list_display = ('mini_descriptions', )
    search_fields = ('mini_descriptions', )
    inlines = [TestimonialsInfoInline]

class ClothesFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions' )
    search_fields = ('title', 'descriptions' )

class LastNewsInfoInline(admin.TabularInline):
    model = models.NewsInline
    extra = 1

class LastNewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions', )
    list_display = ('descriptions', )
    search_fields = ('descriptions', )
    inlines = [LastNewsInfoInline]


admin.site.register(models.News, LastNewsFilterAdmin)
admin.site.register(models.ClothesColor, ClothesFilterAdmin)
admin.site.register(models.Art)
admin.site.register(models.Partner)
admin.site.register(models.Trends)      
admin.site.register(models.Testimonials, TestimonialsFilterAdmin)
admin.site.register(models.Collection, CollectionFilterAdmin)
admin.site.register(models.Discount, DiscountFilterAdmin)
admin.site.register(models.Glance, GlanceFilterAdmin )
admin.site.register(models.Style, StyleFilterAdmin)



# kudbuhon's register
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'mini_description', 'text1', 'text2', 'image1','image2' , 'image3' , 'image4' , 'image5' , 'image6' , 'image7', 'image8', 'image9']

@admin.register(models.Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'question', 'answer']
