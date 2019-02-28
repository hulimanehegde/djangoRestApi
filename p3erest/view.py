from django.http import JsonResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import  HttpResponse


@csrf_exempt
def recipe_list(request):
    result = {}
    print(request.method)
    for recipe in models.Recipe.objects.all():
        print(recipe.name)
        # result.append(dict(name=recipe.name, slug=recipe.slug))

    # result.update({'name': 'slug'})
    return HttpResponse(recipe.name)

