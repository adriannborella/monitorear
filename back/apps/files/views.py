from apps.accounts.models import User
from django import views
from django.http.response import HttpResponse
from .models import Files

class RequestView(views.View):

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        path = request.GET.get('path')
        last_date = request.GET.get('last_date_update')
        token = request.GET.get('token')

        exist = Files.objects.filter(name=name)

        user = User.objects.filter(token=token)        
        if len(user) == 0:
            return HttpResponse('El token no corresponde a ningun usuario')
        
        if len(exist) == 0:
            nuevo = Files(name=name, path=path, last_date_update=last_date, user_id=user.first())
            nuevo.save()
        else:
            actual = exist.first()
            actual.last_date_update = last_date
            actual.save()

        return HttpResponse('Informe Correcto')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')