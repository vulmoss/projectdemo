class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = ["title","content"]
