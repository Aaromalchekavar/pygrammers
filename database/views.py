from django.shortcuts import redirect, render
from .models import Details
# Create your views here.


# detail = {}


def details(req):
    if req.session.has_key('username'):
        if req.session.has_key('password'):
                if req.method == 'POST':

                    name = req.POST['name']
                    bloodgroup = req.POST['bloodgroup']
                    age = req.POST['age']

                    # detail[name] = [bloodgroup, age]

                    data = Details.objects.create(
                        name=name, bloodgroup=bloodgroup, age=age)
                    data.save()

                detail = Details.objects.all()
                return render(req, 'details.html', {'details': detail})
    return redirect('/login')
