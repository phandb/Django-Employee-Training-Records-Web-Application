from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from .models import Task

METHODS = (
    ('', 'Select ...'),
    ('504.1', '504.1'),
    ('508.1 Aroclor', '508.1 Aroclor'),
    ('508.1 Chlordane', '508.1 Chlordane'),
    ('508.1 Pesticides', '508.1 Pesticides'),
    ('508.1 Pesticides-Sublist', '508.1 Pesticides-Sublist'),
    ('508.1 TCEQ-Ind-List', '508.1 TCEQ-Ind-List'),
    ('508.1 Toxaphene', '508.1 Toxaphene'),
    ('508A PCB as DCB', '508A PCB as DCB'),
    ('515.4', '515.4'),
    ('524.2 THM', '524.2 THM'),
    ('524.2 VOC', '524.2 VOC'),
    ('5252 Endrin', '525.2 Endrin'),
    ('525.2 SOC5', '525.2 SOC5'),
    ('531.1 Carbamates', '531.1 Carbamates'),
    ('547 Glyphosate', '547 Glyphosate'),
    ('548.1 Glyphosate', '548.1 Glyphosate'),
    ('548.1 Endothall', '548.1 Endothall'),
    ('549.2 Para_Diq', '549.2 Para/Diq'),
    ('552.2 HAA', '552.2 HAA')
)

CATEGORIES = (
    ('', 'Select ...'),
    ('Extract', 'Extract'),
    ('Analysis', 'Analysis'),
    ('Full Method', 'Full Method')

)


class TaskForm(forms.ModelForm):
    task_name = forms.CharField(
        max_length=100,
        widget=forms.Select(choices=METHODS),
    )
    category = forms.CharField(
        max_length=100,
        widget=forms.Select(choices=CATEGORIES),
    )
    date_taken = forms.DateTimeField(
        input_formats=['%Y/%m/%d %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',

        })
    )

    class Meta:
        model = Task
        fields = [
            'task_name',
            'category',
            'date_taken',
        ]

