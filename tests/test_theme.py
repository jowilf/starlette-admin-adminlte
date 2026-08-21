def test_theme_is_active(admin, theme):
    assert admin.theme is theme


def test_theme_uses_core_icon_set(theme):
    from starlette_admin.theme import CoreIcons

    icon_set = theme.get_icon_set()
    assert isinstance(icon_set, CoreIcons)
    assert icon_set.icons["list.new"] == "fa-solid fa-plus"
    assert icon_set.icons["default_actions.delete"] == "fa-solid fa-trash"


def test_theme_extends_core_icons_with_dark_mode_toggle(theme):
    icons = theme.get_icon_set().icons
    assert icons["nav.dark_mode"] == "fa-solid fa-circle-half-stroke"


def test_class_roles_are_core_vocabulary(theme):
    from starlette_admin.theme import CoreClasses

    # Unmapped roles fall through to CoreClasses, so the map only needs the
    # roles this theme restyles. Every mapped role must exist in the core
    # vocabulary, otherwise it is a typo that silently styles nothing.
    class_map = theme.get_class_map()
    unknown = class_map.classes.keys() - CoreClasses.classes.keys()
    assert not unknown, f"unknown class roles: {sorted(unknown)}"


def test_list_page_loads(client):
    response = client.get("/admin/product/list")
    assert response.status_code == 200


def test_create_page_loads(client):
    response = client.get("/admin/product/create")
    assert response.status_code == 200


def test_theme_stylesheet_is_linked(client):
    # base.html appends the theme stylesheet to the core_css block.
    response = client.get("/admin/product/list")
    assert "css/theme.css" in response.text


def test_icon_stylesheet_is_linked(client):
    response = client.get("/admin/product/list")
    assert "fontawesome.min.css" in response.text


def test_layout_options_enabled_by_default(client):
    html = client.get("/admin/product/list").text
    # Fixed sidebar body class + dark sidebar aside.
    assert "layout-fixed" in html
    assert 'data-bs-theme="dark"' in html
    assert "theme-toggle" in html


def test_layout_options_can_be_disabled(client_flat):
    html = client_flat.get("/admin/product/list").text
    assert "layout-fixed" not in html
    # The aside is the only server-rendered data-bs-theme="dark" element.
    assert 'data-bs-theme="dark"' not in html
