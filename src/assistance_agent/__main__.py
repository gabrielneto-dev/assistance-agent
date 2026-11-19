"""Permite `python -m assistance_agent` (forma portável; ver SPEC-0001 Change Log)."""

from .interfaces.cli import main

raise SystemExit(main())
