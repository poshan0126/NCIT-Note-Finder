from resources.models import ResourceItem
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field, Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import *

class ResourceItemForm(forms.ModelForm):
    class Meta:
        model = ResourceItem
        fields = ('file','course','description', 'tags',)


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
                        Alert(content='<strong>WoW!</strong> You are doing great', css_class = 'alert alert-info'),
                        Alert(content='<strong>Stop!!</strong> Currently, We only accept PDFs and Images.', css_class = 'alert alert-danger'),
                        'file',
                        Alert(content='<strong>Select the exact course for your resource.</strong>', css_class = 'alert alert-info'),
                        'course',
                        Alert(content='<strong>Give a breif description.</strong>', css_class = 'alert alert-dark'),
                        'description',
                        Alert(content='<strong>Enter a comma seperated value. like java, pst, pqt etc.</strong>', css_class = 'alert alert-info'),
                        PrependedText('tags', text = "Give a Relevant Tags:", placeholder="PQT, java, c++, etc")
,


                    ),
                    ButtonHolder(
                        Submit('submit', 'Submit', css_class='btn btn-warning')
                    )
                )

            
    