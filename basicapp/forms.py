from django import forms
from django.core import validators



# def check_for_z(value):
#     if value[0].lower() != "z":
#         raise forms.ValidationError("Name needs to start with Z")



class FormName(forms.Form):
#    name = forms.CharField(validators=[check_for_z])

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter email again", required=True)
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        # clean returns cleaned data for each form fields in dictionary , cleaned data mean after validation.
        # super () - first encounter of this class 16.05.2019 not sure how to handle around it

        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Make sure email match")
########################################
#class MyModelForm(forms.modelForm):
#    class Meta:
#	model = ModelName
#	fields = "__all__" >>>> for all fields from model
#	exclude = ["model_field1","model_field2"] >>>> select all fields and exclude listed
#	fields = ["model_field1", "model_field2"] >>>> from all fields include only listed
