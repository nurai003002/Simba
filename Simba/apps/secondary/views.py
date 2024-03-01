from django.shortcuts import render
from apps.secondary.models import About, Faqs
# Create your views here.
def about(request):
    about = About.objects.latest("id")
    return render(request, "about.html", locals())

def faqs(request):
    faqs = Faqs.objects.latest("id")
    faqs_all = Faqs.objects.all()
    return render(request, "faqs.html", locals())

