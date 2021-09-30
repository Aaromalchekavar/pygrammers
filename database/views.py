from django.shortcuts import render
from .models import Details
# Create your views here.


# detail = {}


def details(req):

    # name = req.POST['name']
    # bloodgroup = req.POST['bloodgroup']
    # age = req.POST['age']

    # detail[name] = [bloodgroup, age]

    detail = Details.objects.all()

    return render(req, 'details.html', {'details': detail})