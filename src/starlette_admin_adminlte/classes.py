"""Class map for the AdminLTE theme.

Core templates render class attributes through `cls('role.name')`. This map
overrides the roles this theme restyles; any role left unmapped falls through
to the Tabler defaults in `CoreClasses`, so a partial map is always safe.

The role vocabulary lives in `starlette_admin.theme.CoreClasses`. A button
role owns the element's whole class attribute (variant, size, and spacing
included), so mapping it replaces the button's look wholesale.
"""

from __future__ import annotations

from starlette_admin.theme import ClassMap


class AdminlteClasses(ClassMap):
    """Overrides for the component roles this theme restyles.

    Bootstrap/AdminLTE leaves a bare `.btn` transparent, so every secondary
    action here adds `btn-outline-secondary` for a visible border.
    """

    classes = {
        "action.button": "btn btn-outline-secondary",
        "action.dropdown_toggle": "btn btn-outline-secondary dropdown-toggle",
        "filter.chip": (
            "badge rounded-pill bg-primary-subtle text-primary-emphasis "
            "text-decoration-none d-inline-flex align-items-center gap-1"
        ),
        "filter.toggle_button": "btn btn-outline-secondary dropdown-toggle",
        "filter.add_condition_button": "btn btn-sm btn-outline-secondary",
        "filter.add_group_button": "btn btn-sm btn-outline-secondary",
        "form.save_add_button": "btn btn-outline-secondary",
        "form.save_continue_button": "btn btn-outline-secondary",
        "inline_edit.cancel_button": "btn btn-outline-secondary btn-icon",
        "list.search_button": "btn btn-outline-secondary",
        "list.columns_toggle": "btn btn-outline-secondary dropdown-toggle",
        "list.import_button": "btn btn-outline-secondary",
        # Tabler's "btn-block" isn't a Bootstrap 5 class; drop it.
        "list.create_button": "btn btn-primary ms-2",
        # Tabler's "steps"/"step-item" ship with Tabler's own CSS bundle and
        # render unstyled under AdminLTE; theme.css styles these instead.
        "steps.container": "wizard-steps",
        "steps.item": "wizard-step",
    }
