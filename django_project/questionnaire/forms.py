from django import forms
from .models import Question


class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(Question.objects.all()):
            self.fields['%s_field' % i] = forms.CharField(max_length=100, label=q.question_text)