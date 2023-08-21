from django.db import models
from django.forms import fields
from django import forms

from .models import WallSection, Route


class WallSectionForm(forms.ModelForm):
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = WallSection
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super().__init__(*args, **kwargs)
        self.fields['extra_field_count'].inital = extra_fields

        for index in range(int(extra_fields)+1):
            # generate extra fields in the number specified via extra_fields
            self.fields['grade_{index}'.format(index=index)] = forms.IntegerField()
            self.fields['colour_{index}'.format(index=index)] = forms.CharField()

    def save(self):
        super().save()
        wall_section = self.instance
        wall_section.route_set.all().delete()

        i = 0
        grade_field = 'grade_%s' % (i,)
        colour_field = 'colour_%s' % (i,)
        while (self.cleaned_data.get(grade_field) and self.cleaned_data.get(colour_field)):
           Route.objects.create(
               wall_section=wall_section,
               grade=self.cleaned_data.get(grade_field),
               colour=self.cleaned_data.get(colour_field),
           )
           i += 1
           grade_field = 'grade_%s' % (i,)
           colour_field = 'colour_%s' % (i,)
