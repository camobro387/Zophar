from django import forms
from .models import Question


class QuestionForm(forms.Form):

    m = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    w = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))
    r = ((1, '10%'), (2, '20%'), (3, '30%'), (4, '40%'), (5, '50%'),
         (6, '60%'), (7, '70%'), (8, '80%'), (9, '90%'), (10, '100%'))

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for i, q in enumerate(Question.objects.all()):
            if q.type == 'm':
                self.fields['%s_field' % i] = forms.ChoiceField(
                    widget=forms.RadioSelect,
                    choices=self.m,
                    label=q.question_text)
            if q.type == 'w':
                self.fields['%s_field' % i] = forms.ChoiceField(
                    widget=forms.RadioSelect,
                    choices=self.w,
                    label=q.question_text)
            if q.type == 'r':
                self.fields['%s_field' % i] = forms.ChoiceField(
                    widget=forms.RadioSelect,
                    choices=self.r,
                    label=q.question_text)
            if q.type == 'b':
                self.fields['%s_field' % i] = forms.BooleanField(label=q.question_text)

