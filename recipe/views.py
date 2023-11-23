from django.shortcuts import render

from recipe.models import Recipe


def list(request):
    template_name = 'recipe/list.html'

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, template_name, context)


def detail(request, pk):
    template_name = 'recipe/detail.html'
    recipe = Recipe.objects.get(pk=pk)
    recipe_instructions = recipe.instructions.split('\n')

    context = {
        'recipe': recipe,
        'recipe_instructions': recipe_instructions,
    }

    return render(request, template_name, context)
