"""SPEC-0001/AC-002: `core` e `ports` não dependem de `adapters` nem de `interfaces`."""

import ast
from pathlib import Path

import pytest

PACKAGE = "assistance_agent"
SRC = Path(__file__).resolve().parents[1] / "src"
PROTECTED_LAYERS = ("core", "ports")
FORBIDDEN_PREFIXES = (f"{PACKAGE}.adapters", f"{PACKAGE}.interfaces")


def module_name(path: Path) -> str:
    parts = list(path.relative_to(SRC).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def imported_modules(source: str, current_module: str, is_package: bool) -> set[str]:
    """Nomes absolutos de todos os módulos importados por `source`."""
    package_parts = current_module.split(".") if is_package else current_module.split(".")[:-1]
    found: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = package_parts[: len(package_parts) - node.level + 1]
                prefix = ".".join(base)
                module = f"{prefix}.{node.module}" if node.module else prefix
            else:
                module = node.module or ""
            found.add(module)
            found.update(f"{module}.{alias.name}" for alias in node.names)
    return found


def forbidden_imports(source: str, current_module: str, is_package: bool = False) -> list[str]:
    return sorted(
        name
        for name in imported_modules(source, current_module, is_package)
        if any(name == p or name.startswith(p + ".") for p in FORBIDDEN_PREFIXES)
    )


def protected_files() -> list[Path]:
    return [
        path for layer in PROTECTED_LAYERS for path in sorted((SRC / PACKAGE / layer).rglob("*.py"))
    ]


def test_protected_layers_exist() -> None:
    for layer in (*PROTECTED_LAYERS, "adapters", "interfaces"):
        assert (SRC / PACKAGE / layer / "__init__.py").is_file(), layer


@pytest.mark.parametrize("path", protected_files(), ids=lambda p: module_name(p))
def test_core_and_ports_do_not_import_outer_layers(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    bad = forbidden_imports(source, module_name(path), path.name == "__init__.py")
    assert bad == [], f"{module_name(path)} importa camadas externas: {bad}"


@pytest.mark.parametrize(
    "source",
    [
        "import assistance_agent.adapters.fake_llm",
        "from assistance_agent.interfaces import cli",
        "from ..adapters import fake_llm",
        "from ..interfaces.cli import main",
    ],
)
def test_checker_detects_planted_forbidden_import(source: str) -> None:
    assert forbidden_imports(source, "assistance_agent.core.conversation") != []


def test_checker_allows_ports_and_stdlib() -> None:
    source = "import asyncio\nfrom ..ports.llm import LLMClient\nfrom . import tenant\n"
    assert forbidden_imports(source, "assistance_agent.core.conversation") == []
