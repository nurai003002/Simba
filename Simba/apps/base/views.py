from django.shortcuts import render
from apps.base.models import Settings,Slide
from apps.secondary import models

# Create your views here.
def index(request):
    slide = Slide.objects.all()
    style = models.Style.objects.latest('id')
    glance = models.Glance.objects.latest('id')
    discount = models.Discount.objects.all()
    collection = models.Collection.objects.latest('id')
    testimonials = models.Testimonials.objects.latest('id')
    trend = models.Trends.objects.latest('id')
    partner = models.Partner.objects.all()
    art = models.Art.objects.all()
    clothes_color = models.ClothesColor.objects.latest('id')
    lastnews = models.News.objects.latest('id')
    return render(request, 'index-2.html', locals())
