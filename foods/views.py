from django.views.generic import ListView
from .models import Food

class HomePageView(ListView):
    model = Food
    template_name = "foods/index.html"
 