from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # Django にフォームを作るときにどのモデルを使えばいいかを伝える
    # formのfieldsに何を書けばいいかを伝える
    class Meta:
        model = Post
        fields = ('title', 'text',)