from django import forms
from tasks.models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("title python is not allowed")
        return title

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("content")
        title = cleaned_data.get("title")
        if title and description and title.lower() == description.lower():
            raise forms.ValidationError("title and content should not be same")
        return cleaned_data



class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False, widget=forms.Select
    )
    orderings = (
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания(по убыванию"),
        ("title", "По названию"),
        ("-title", "По названию(по убыванию" ),
        ("rate", "По рейтингу"),
        ("-rate", "По рейтингу(по убыванию)"),
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)

