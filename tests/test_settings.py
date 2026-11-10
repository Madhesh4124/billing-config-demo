"""Unit tests verifying v23.2.0 attrs behavior."""

from billing.settings import BillingSettings, clone_with_endpoint, clone_with_timeout


def test_clone_with_timeout():
    cfg = BillingSettings(endpoint="https://api.example.com", timeout_seconds=5)
    updated = clone_with_timeout(cfg, timeout_seconds=20)
    assert updated.timeout_seconds == 20
    assert updated.endpoint == "https://api.example.com"


def test_clone_with_endpoint():
    cfg = BillingSettings(endpoint="https://api.example.com")
    updated = clone_with_endpoint(cfg, "https://v2.example.com")
    assert updated.endpoint == "https://v2.example.com"
