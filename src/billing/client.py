"""HTTP client helper built with httpx."""

import httpx


def fetch_billing_status(url: str) -> int:
    """Perform a simple GET request and return the HTTP status code."""
    with httpx.Client(timeout=5.0) as client:
        response = client.get(url)
        return response.status_code
