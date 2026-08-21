# starlette-admin-adminlte

An [AdminLTE 4](https://adminlte.io) theme for [starlette-admin](https://github.com/jowilf/starlette-admin).

This package replaces the default Tabler look with AdminLTE's classic layout. It provides a fixed dark sidebar, a top navbar with a sidebar toggle, Bootstrap 5 components, and a built-in light/dark mode toggle.

## Requirements

* Python 3.11 or higher
* starlette-admin 1.0.0 or higher

## Installation

The package is currently distributed exclusively via GitHub rather than PyPI.

Using `pip`:

```bash
pip install git+https://github.com/jowilf/starlette-admin-adminlte.git

```

Using [`uv`](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/jowilf/starlette-admin-adminlte.git

```

*Note: To pin a specific version, append `@<tag-or-commit>` to the repository URL.*

## Usage

Integration requires only a single step. Pass the `AdminlteTheme` instance to your `Admin` constructor:

```python
from starlette_admin.contrib.sqla import Admin
from starlette_admin_adminlte import AdminlteTheme

admin = Admin(engine, theme=AdminlteTheme())

```

This theme is fully compatible with every `starlette-admin` backend, including `contrib.sqla`, `contrib.mongoengine`, and `contrib.odm`.

## Configuration Options

You can customize the theme by passing arguments to the `AdminlteTheme` constructor. These options are also exposed globally to templates via the `theme_config` variable.

```python
theme = AdminlteTheme(dark_sidebar=False, fixed_sidebar=False)

```

| Option | Default | Description |
| --- | --- | --- |
| `dark_sidebar` | `True` | Renders the sidebar using AdminLTE's dark variant. |
| `fixed_sidebar` | `True` | Pins the sidebar in place so only the main content area scrolls. |

## What's Included

* **Layout (`templates/layout.html`)**: Renders the complete AdminLTE 4 shell. This includes the top navbar with a sidebar toggle, dark mode switch, language and timezone selectors, and a user menu. It also includes the collapsible sidebar with treeview dropdowns and the main content container.
* **Login Page (`templates/login.html`)**: Restyles the default login form to include a show/hide password toggle and a "remember me" checkbox.
* **Class Mapping (`classes.py`)**: Overrides the CSS classes of core component roles to match Bootstrap 5 styles (e.g., buttons, filter chips, wizard steps). Any unmapped roles inherit their core defaults.
* **Static Assets**: Includes vendored dependencies for AdminLTE, Bootstrap, and OverlayScrollbars under the `static/` directory. Visual overrides are provided in `static/css/theme.css`.
* **Dark/Light Mode**: Resolved before the first paint using the `localStorage` key `lte-theme`. If no preference is saved locally, it falls back to the user's OS preference.

## Overriding Templates and Assets

In the template loader chain, a theme takes precedence over plugins but yields to user overrides. The exact precedence order is: **user > theme > plugins > core**.

To override a theme file, place a file with the identical name and path inside your application's `templates_dir` or `static_dir`. For example:

```text
your_app/templates/
└── layout.html        # Overrides the theme's layout.html

```

If your custom override needs to extend this theme's template rather than the core template, use the `@theme` prefix. This prefix explicitly resolves to the theme's original file:

```jinja
{% extends "@theme/base.html" %}

```

## Example Application

The repository includes a runnable demonstration that exercises every field type, filter, action, inline form, relation, dashboard widget, and custom route supported by `starlette-admin`.

To run the example locally:

```bash
git clone https://github.com/jowilf/starlette-admin-adminlte.git
cd starlette-admin-adminlte
uv sync
uv run python example/app.py

```

Once the server is running, navigate to `http://localhost:8000/admin/` and log in with the credentials `admin` / `admin`.

## Development

To set up the development environment and run quality checks:

```bash
uv sync          # Install dev dependencies
make test        # Run the test suite
make lint        # Run Ruff check and format check
make format      # Auto-fix linting issues and format code

```

**Translation Management**

Managing translation messages requires the `i18n` extra. First, run `uv sync --extra i18n`, then use the following commands:

```bash
make extract-messages    # Rebuild the messages.pot template
make update-messages     # Merge changes into .po catalogs
make compile-messages    # Compile into .mo files
```

## License

MIT