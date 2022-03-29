from django import forms
class AddTaskForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Title"}), label="")
    task_body = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Info"}), label="")
    date_end = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'], widget=forms.DateTimeInput(attrs={"class":"form-control", "id":"datetimepicker","placeholder":"Set Time"}), label="")

