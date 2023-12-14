from django.contrib import messages
from django.shortcuts import render

from recipe.forms import AddCommentForm
from recipe.models import Comment, Recipe


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
    comments = Comment.objects.all().filter(recipe=recipe)
    recipe_instructions = recipe.instructions.split('\n')
    form = AddCommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        Comment.objects.create(
            text=form.cleaned_data['text'],
            user=request.user,
            recipe=recipe,
        )
        messages.info(request, 'После модерации ваш комментарий будет добавлен')

    context = {
        'recipe': recipe,
        'recipe_instructions': recipe_instructions,
        'comments': comments,
        "form": form,
    }

    return render(request, template_name, context)
