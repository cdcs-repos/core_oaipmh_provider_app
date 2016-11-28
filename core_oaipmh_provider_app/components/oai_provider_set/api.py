"""
OaiProviderSet API
"""

from core_oaipmh_provider_app.components.oai_provider_set.models import OaiProviderSet


def upsert(oai_provider_set):
    """ Create or update an OaiProviderSet.

    Args:
        oai_provider_set:

    Returns:
        The OaiProviderSet instance.

    """
    return oai_provider_set.save()


def delete(oai_provider_set):
    """ Delete an OaiProviderSet.

    Args:
        oai_provider_set: The OaiProviderSet to delete.

    """
    oai_provider_set.delete()


def get_by_id(oai_provider_set_id):
    """ Get an OaiProviderSet by its id.

    Args:
        oai_provider_set_id: The OaiProviderSet id.

    Returns:
        The OaiProviderSet instance.

    """
    return OaiProviderSet.get_by_id(oai_set_id=oai_provider_set_id)


def get_by_set_spec(set_spec):
    """ Get an OaiProviderSet by its set_spec.

    Args:
        set_spec: The OaiProviderSet set_spec.

    Returns:
        The OaiProviderSet instance.
    """
    return OaiProviderSet.get_by_set_spec(set_spec=set_spec)


def get_all():
    """ Get all OaiProviderSet.

    Returns:
        List of OaiProviderSet.
    """
    return OaiProviderSet.get_all()


def get_all_by_templates(templates):
    """ Get all OaiProviderSet used by a list of templates.

    Args:
        templates: List of templates.

    Returns:
        List of OaiProviderSet.

    """
    return OaiProviderSet.get_all_by_templates(templates=templates)
