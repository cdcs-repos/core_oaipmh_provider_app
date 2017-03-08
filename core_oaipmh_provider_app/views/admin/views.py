from django.contrib.admin.views.decorators import staff_member_required
from core_main_app.utils.rendering import admin_render
from core_oaipmh_provider_app.components.oai_settings import api as oai_settings_api
from core_oaipmh_provider_app import settings


@staff_member_required
def identity_view(request):
    assets = {
        "js": [
            {
                "path": "core_oaipmh_provider_app/admin/js/registry/identity/check_registry.js",
                "is_raw": False
            },
            {
                "path": "core_oaipmh_provider_app/admin/js/registry/identity/modals/edit_identity.js",
                "is_raw": False
            }
        ],
        "css": [
            "core_oaipmh_provider_app/admin/css/registry/identity/table_info.css"
        ]
    }

    modals = [
        "core_oaipmh_provider_app/admin/registry/identity/modals/edit_identity.html"
    ]

    info = oai_settings_api.get()
    data_provider = {
        'name': info.repository_name,
        # FIXME: use reverse('oai_server_xxx') when developed
        'baseURL': settings.OAI_HOST_URI + "/oai_pmh/server/",
        'protocol_version': settings.OAI_PROTOCOL_VERSION,
        'admins': (email for name, email in settings.OAI_ADMINS),
        'deleted': settings.OAI_DELETED_RECORD,
        'granularity': settings.OAI_GRANULARITY,
        'identifier_scheme': settings.OAI_SCHEME,
        'repository_identifier': info.repository_identifier,
        'identifier_delimiter': settings.OAI_DELIMITER,
        'sample_identifier': settings.OAI_SAMPLE_IDENTIFIER,
        'enable_harvesting': info.enable_harvesting,
    }

    context = {
        "data_provider": data_provider
    }

    return admin_render(request, "core_oaipmh_provider_app/admin/registry/identity.html", assets=assets,
                        context=context, modals=modals)
