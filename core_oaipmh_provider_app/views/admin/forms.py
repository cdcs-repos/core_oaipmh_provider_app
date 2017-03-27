from django import forms
from core_main_app.components.template_version_manager import api as template_version_manager_api
from core_main_app.components.template import api as template_api


class EditIdentityForm(forms.Form):
    """
        An identity update form.
    """
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    repository_identifier = forms.CharField(label='Repository Identifier', required=True,
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    enable_harvesting = forms.BooleanField(label='Enable Harvesting ?',
                                           widget=forms.CheckboxInput(attrs={'class': 'cmn-toggle cmn-toggle-round',
                                                                             'visibility': 'hidden'}),
                                           required=False, initial=False)
    id = forms.CharField(widget=forms.HiddenInput(), required=False)


class MetadataFormatForm(forms.Form):
    """
        A metadata format form.
    """
    metadata_prefix = forms.CharField(label='Metadata Prefix', required=True,
                                      widget=forms.TextInput(attrs={'placeholder': 'example: oai_dc',
                                                                    'class': 'form-control'}))
    schema = forms.URLField(label='Schema URL', required=True, widget=forms.URLInput(attrs={'class': 'form-control'}))


class EditMetadataFormatForm(forms.Form):
    """
        A metadata format update form.
    """
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    metadata_prefix = forms.CharField(label='Metadata Prefix', required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))


class TemplateMetadataFormatForm(forms.Form):
    """
        A template metadata format form.
    """
    metadata_prefix = forms.CharField(label='Metadata Prefix', required=True,
                                      widget=forms.TextInput(attrs={'placeholder': 'example: oai_dc',
                                                                    'class': 'form-control'}))
    template = forms.ChoiceField(label='Template', widget=forms.Select(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super(TemplateMetadataFormatForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices = _get_templates_versions()


class SetForm(forms.Form):
    """
        A set form.
    """
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    set_spec = forms.CharField(label='Set spec', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    set_name = forms.CharField(label='Set name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    templates_manager = forms.MultipleChoiceField(label='Templates', widget=forms.SelectMultiple())
    description = forms.CharField(label='Description', required=True,
                                  widget=forms.Textarea(attrs={'cols': '60', 'rows': '5', 'class': 'form-control',
                                                               'style': 'height:14em;width:100%;'}))

    def __init__(self, *args, **kwargs):
        super(SetForm, self).__init__(*args, **kwargs)
        self.fields['templates_manager'].choices = _get_templates_manager()


def _get_templates_versions():
    """ Get templates versions.

    Returns:
        List of templates versions.

    """
    templates = []
    try:
        list_ = template_version_manager_api.get_active_global_version_manager()
        for elt in list_:
            for version in elt.versions:
                version_name = "{0} (Version {1})".format(elt.title,
                                                          template_version_manager_api.get_version_number(elt, version))
                templates.append((version, version_name))
    except Exception:
        pass

    return templates


def _get_templates_manager():
    """ Get templates manager.

    Returns:
        List of templates manager.

    """
    templates_manager = []
    try:
        list_ = template_version_manager_api.get_active_global_version_manager()
        for elt in list_:
            templates_manager.append((elt.id, elt.title))
    except Exception:
        pass

    return templates_manager