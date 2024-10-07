from django.shortcuts import render
from myapp.models import books
from django.http import HttpResponse

# Create your views here.
def index(request):
  if request.method == "POST":
    data = request.POST
    print(data)
    new = books(author = data["field1"], name = data["field2"], description = data["field3"], size = data["field4"])
    new.save()
  res = books.objects.all()
  return render(request, "index.html", {"test":res})


def fullCard(request, myid):
  set = books.objects.filter(id = myid)
  return render(request, 'card.html', {"set":set})