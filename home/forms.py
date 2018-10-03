from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from partners.models import CampusPartner, CommunityPartner
from university.models import *
from home.models import  Contact
from django.utils.translation import ugettext_lazy as _
from projects.models import Project, EngagementType, ActivityType, Status, ProjectCampusPartner, ProjectCommunityPartner
from django.forms import ModelForm


class CampusPartnerUserForm(forms.ModelForm):

    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s</p>%(field)s%(help_text)s',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

    class Meta:
        model = CampusPartner
        fields = ('name',)

    name = forms.ModelChoiceField(
        queryset=CampusPartner.objects.order_by().distinct('name'),
        label='Campus Partner Name', help_text='Please Register Your Organization if not found in list')


class CampusPartnerForm(forms.ModelForm):

    class Meta:
        model = CampusPartner
        fields = ('name', 'education_system','university', 'college', 'department',)




class CommunityPartnerUserForm(forms.ModelForm):

    class Meta:
        model = CommunityPartner
        fields = ('name',)

    name = forms.ModelChoiceField(
        queryset=CommunityPartner.objects.order_by().distinct('name'),
                                 label='Community Partner Name',help_text='Please Register your Organization if not found in list')



class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email' )
        help_texts = {
            'username': None,
            'email': None,
        }

        labels = {
            'username': ('User Name'),
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'email': ('Email ID')
        }


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CommunityPartnerForm(forms.ModelForm):
    class Meta:
        model = CommunityPartner
        fields = ('name', 'website_url', 'community_type', 'k12_level', 'address_line1', 'address_line2', 'country', 'city', 'state', 'Zip')


class CommunityContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name',
                  'last_name',
                  'workphone',
                  'cellphone',
                  'email_id',
                  'contact_type')


class ProjectForm(forms.ModelForm):
    engagement_type = forms.ModelChoiceField(queryset=EngagementType.objects.all(), to_field_name="name")
    activity_type = forms.ModelChoiceField(queryset=ActivityType.objects.all(), to_field_name="name")
    status = forms.ModelChoiceField(queryset=Status.objects.all(), to_field_name="name")

    class Meta:
        model = Project
        fields = ('name', 'engagement_type', 'activity_type', 'facilitator', 'description', 'semester',
                  'total_uno_students', 'total_uno_hrs', 'total_k12_students', 'total_k12_hrs', 'total_uno_faculty',
                  'total_other_community_members', 'other_details', 'outcomes', 'total_economic_impact', 'status')


class ProjectCampusPartnerForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Project.objects.all(), to_field_name="name")
    campus_partner = forms.ModelChoiceField(queryset=CampusPartner.objects.all(), to_field_name="name")

    class Meta:
        model = ProjectCampusPartner
        fields = ('name', 'campus_partner')


class CommunityForm(ModelForm):
    class Meta:
        model = CommunityPartner
        fields = '__all__'


class CampusForm(ModelForm):

    class Meta:
        model = CampusPartner
        fields = '__all__'
        TRUE_FALSE_CHOICES = (
            ('True', 'Yes'),
            ('False', 'No'),
        )
        weitz_cec_part = forms.ChoiceField(widget=forms.Select(choices=TRUE_FALSE_CHOICES))


