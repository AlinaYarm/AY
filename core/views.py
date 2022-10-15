from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from core import models


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['person_name'] = 'Masha'
        return c

class Person(ListView):
    model = models.Person

    #def get(self, request, *args, **kwargs):
        # response = super().get(request, *args, **kwargs)
        # return response
        # object_list = []
        # for p in models.Person.objects.all():
        #     object_list.append({
        #         'id': p.id,
        #         'name': p.name,
        #     })
        # return JsonResponse({'results': object_list})

# def index(request):
#     #now = timezone.now()
#     person = models.Person.objects.first()
#     #response = HttpResponse(f'<h1>Hello World!<h1>{now}')
#     response = render(request, 'core/index.html', context={'person': person})
#     return response

# def persons (request):
#     object_list = []
#     for p in models.Person.objects.all():
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#         })
#     #content = json.dumps(object_list)
#     return JsonResponse({'results': object_list})

def persons(request, id):
    if request.method == 'GET':
        p = get_object_or_404(models.Person, id=id)
        detail = {
            'id': p.id,
            'name': p.name,
            'phone': p.phone,
        }
        return JsonResponse(detail)
    #elif request.method == ''
