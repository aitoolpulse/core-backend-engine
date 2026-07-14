"""Resolve TIYAZO_HOME for standalone skill scripts.

Skill scripts may run outside the Hermes process (e.g. system Python,
nix env, CI) where ``tiyazo_constants`` is not importable.  This module
provides the same ``get_tiyazo_home()`` and ``display_tiyazo_home()``
contracts as ``tiyazo_constants`` without requiring it on ``sys.path``.

When ``tiyazo_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``tiyazo_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``TIYAZO_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from tiyazo_constants import display_tiyazo_home as display_tiyazo_home
    from tiyazo_constants import get_tiyazo_home as get_tiyazo_home
except (ModuleNotFoundError, ImportError):

    def get_tiyazo_home() -> Path:
        """Return the Hermes home directory (default: ~/.tiyazo).

        Mirrors ``tiyazo_constants.get_tiyazo_home()``."""
        val = os.environ.get("TIYAZO_HOME", "").strip()
        return Path(val) if val else Path.home() / ".tiyazo"

    def display_tiyazo_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``tiyazo_constants.display_tiyazo_home()``."""
        home = get_tiyazo_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
