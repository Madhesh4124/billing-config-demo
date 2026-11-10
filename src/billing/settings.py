"""Service configuration helpers built with attrs."""

import attrs
from attrs import define, evolve


@define
class BillingSettings:
    """Configuration for downstream billing API calls."""

    endpoint: str
    timeout_seconds: int = 5


def clone_with_timeout(cfg: BillingSettings, timeout_seconds: int = 15) -> BillingSettings:
    """Return updated settings using the `inst=` keyword argument removed in attrs 24.1.0."""
    return attrs.evolve(inst=cfg, timeout_seconds=timeout_seconds)


def clone_with_endpoint(cfg: BillingSettings, endpoint: str) -> BillingSettings:
    """Update endpoint via direct from-imported evolve call."""
    return evolve(inst=cfg, endpoint=endpoint)
