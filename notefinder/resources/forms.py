from resources.models import ResourceItem, ResourceURL
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field, Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import *
import os

class ResourceItemForm(forms.ModelForm):
    class Meta:
        model = ResourceItem
        fields = ('title', 'file','course','description', 'tags',)


    def __init__(self, *args, **kwargs):
        super(ResourceItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ResourceItemForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''

        # self.helper.add_input(Submit('submit', 'Submit'))
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Fieldset(
                        'Upload New File',
                        Alert(content='<strong>WoW!</strong> You are doing great</br></br> <strong>Stop!!</strong> Currently, We only accept .pdf, .docx, .doc, .png, .jpeg, .jpg, .ppt, .xlxs, .txt, ODT, FODT, ODS, FODS, ODP, FODP, ODG, FODG, ODF, .rst</br></br><strong></br></br>Uploading of any file, except above accepted file format will results in automatic disqualification.', css_class = 'alert alert-info'),
                        'title',
                        'file',
                        Alert(content='<strong>Select the exact course for your resource.</strong>', css_class = 'alert alert-info'),
                        'course',
                        Alert(content='<strong>Give a breif description.</strong>', css_class = 'alert alert-dark'),
                        'description',
                        'tags'
,


                    ),
                    ButtonHolder(
                        Submit('submit', 'Submit', css_class='btn btn-warning')
                    )
                )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     file_name = cleaned_data.get("file").name
    #     extension = file_name.split('.')[1:]
    #     extension = "".join(extension)
    #     accepted_extension = ["pdf", "docx", "doc", "png", "jpeg", "jpg", "ppt", "xlxs", "txt", "ODT", "FODT", "ODS", "FODS", "ODP", "FODP", "ODG", "FODG", "ODF", "rst"]
    #     if extension not in accepted_extension:
    #         raise forms.ValidationError(
    #                 "We cannot accept your file, Did you check your file format."
    #             )
    #         self.add_errors("file", "Sorry")

    def clean_file(self):
        file = self.cleaned_data.get('file')
        file_name = file.name
        extension = file_name.split('.')[1:]
        extension = "".join(extension)
        accepted_extension = ["pdf", "docx", "doc", "png", "jpeg", "jpg", "ppt", "xlxs", "txt", "ODT", "FODT", "ODS", "FODS", "ODP", "FODP", "ODG", "FODG", "ODF", "rst"]
        if extension not in accepted_extension:
            raise forms.ValidationError("Currently We hate .{}".format(extension))
        return file




class ResourceURLForm(forms.ModelForm):
    class Meta:
        model = ResourceURL
        fields = ('title','url','course','description', 'tags',)


    def __init__(self, *args, **kwargs):
        super(ResourceURLForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ResourceURLForm'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''

        # self.helper.add_input(Submit('submit', 'Submit'))
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    Fieldset(
                        'Register a New URL',
                        Alert(content='<strong>Thanks for your effort!!. </br></br> You are keeping our community alive.</br></br>Uploading of spam URLs will result in automatic disqualification and Peanalised the IP address.</strong>.', css_class = 'alert alert-info'),
                        'title',
                        'url',
                        Alert(content='<strong>Select the exact course for your resource.</strong>', css_class = 'alert alert-info'),
                        'course',
                        Alert(content='<strong>Give a breif description.</strong>', css_class = 'alert alert-dark'),
                        'description',
                        'tags'
,


                    ),
                    ButtonHolder(
                        Submit('submit', 'Submit', css_class='btn btn-warning')
                    )
                )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     file_name = cleaned_data.get("file").name
    #     extension = file_name.split('.')[1:]
    #     extension = "".join(extension)
    #     accepted_extension = ["pdf", "docx", "doc", "png", "jpeg", "jpg", "ppt", "xlxs", "txt", "ODT", "FODT", "ODS", "FODS", "ODP", "FODP", "ODG", "FODG", "ODF", "rst"]
    #     if extension not in accepted_extension:
    #         raise forms.ValidationError(
    #                 "We cannot accept your file, Did you check your file format."
    #             )
    #         self.add_errors("file", "Sorry")

    # def clean_file(self):
    #     file = self.cleaned_data.get('file')
    #     file_name = file.name
    #     extension = file_name.split('.')[1:]
    #     extension = "".join(extension)
    #     accepted_extension = ["pdf", "docx", "doc", "png", "jpeg", "jpg", "ppt", "xlxs", "txt", "ODT", "FODT", "ODS", "FODS", "ODP", "FODP", "ODG", "FODG", "ODF", "rst"]
    #     if extension not in accepted_extension:
    #         raise forms.ValidationError("Currently We hate .{}".format(extension))
    #     return file