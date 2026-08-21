"""`AdminlteTheme`: the active theme passed to `Admin(theme=...)`.

A theme owns the admin layout and styling. Its surface is intentionally small:
replacement templates at bare paths, an `IconSet`, a `ClassMap`, and template
globals. Exactly one theme is active per `Admin` instance. See the theme
module docstring in starlette-admin for the full contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from starlette_admin.theme import (
    BaseTheme,
    ClassMap,
    CoreIcons,
    IconSet,
)

from .classes import AdminlteClasses


class AdminlteIcons(CoreIcons):
    """The core FontAwesome vocabulary plus this theme's additions."""

    icons = {
        **CoreIcons.icons,
        "nav.dark_mode": "fa-solid fa-circle-half-stroke",
    }


@dataclass(frozen=True)
class AdminlteConfig:
    """Options accepted by `AdminlteTheme(**options)`.

    Every option is exposed to templates via the `theme_config` global.
    """

    #: Render the sidebar with AdminLTE's dark variant.
    dark_sidebar: bool = True

    #: Pin the sidebar so it stays put while the main content scrolls.
    fixed_sidebar: bool = True


class AdminlteTheme(BaseTheme):
    """AdminLTE 4 theme for starlette-admin.

    Replaces the default Tabler look with AdminLTE's classic layout: fixed
    dark sidebar, top navbar with sidebar toggle, Bootstrap 5 components,
    and a light/dark mode toggle. Light/dark is resolved before first paint
    from `localStorage`, falling back to the OS preference, so the theme
    needs no server-side color-mode state.
    """

    name = "adminlte"

    # Import package holding this theme's templates/ and static/ folders.
    package = "starlette_admin_adminlte"

    def __init__(
        self,
        *,
        dark_sidebar: bool = True,
        fixed_sidebar: bool = True,
    ) -> None:
        """Create the theme from explicit options (IDE-autocompletable).

        Args:
            dark_sidebar: Render the sidebar with AdminLTE's dark variant.
            fixed_sidebar: Pin the sidebar so it stays put while the main
                content scrolls.
        """
        self.config = AdminlteConfig(
            dark_sidebar=dark_sidebar,
            fixed_sidebar=fixed_sidebar,
        )

    def get_icon_set(self) -> IconSet:
        return AdminlteIcons()

    def get_class_map(self) -> ClassMap:
        return AdminlteClasses()

    def template_globals(self) -> dict[str, Any]:
        # Theme globals are exposed unprefixed (unlike plugin globals).
        return {"theme_config": self.config}
