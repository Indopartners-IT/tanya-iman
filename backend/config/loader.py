"""Loaders for the YAML and prompt files that gate deployment.

Every loader is cached, so a config change requires a restart. That is
deliberate: config in this project includes crisis scripts and answer prompts,
and hot-reloading either of those is not a property we want.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

CONFIG_DIR = Path(__file__).parent
PROMPT_DIR = CONFIG_DIR / "prompts"


def _read_yaml(name: str) -> dict[str, Any]:
    with (CONFIG_DIR / name).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


@lru_cache
def approved_sites() -> dict[str, Any]:
    return _read_yaml("approved_sites.yml")


@lru_cache
def approved_domains() -> frozenset[str]:
    return frozenset(s["domain"] for s in approved_sites().get("sites", []))


@lru_cache
def responses() -> dict[str, str]:
    return _read_yaml("responses.id.yml")


@lru_cache
def crisis_config() -> dict[str, Any]:
    return _read_yaml("crisis_scripts.id.yml")


@lru_cache
def topics() -> list[dict[str, str]]:
    return _read_yaml("topics.yml").get("topics", [])


@lru_cache
def topic_slugs() -> frozenset[str]:
    return frozenset(t["slug"] for t in topics())


@lru_cache
def prompt(name: str) -> str:
    """Load a prompt file, stripping comment lines.

    Comment lines carry review gates and provenance for humans; sending them to
    a model wastes tokens and, worse, tells it about its own review process.
    """
    text = (PROMPT_DIR / f"{name}.txt").read_text(encoding="utf-8")
    body = "\n".join(line for line in text.splitlines() if not line.startswith("#"))
    return body.strip()


def response(key: str, **kwargs: object) -> str:
    """Fetch a canonical response string, interpolating any placeholders."""
    template = responses()[key]
    return template.format(**kwargs) if kwargs else template
