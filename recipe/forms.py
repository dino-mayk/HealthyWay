from core.forms import AbstractModelForm
from recipe.models import Comment


class AddCommentForm(AbstractModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
        )