from __future__ import annotations

from typing import Protocol

from config import get_settings

DEV_CODE = "000000"


class OTPProvider(Protocol):
    name: str

    async def send(self, phone_e164: str, channel: str) -> None: ...

    async def verify(self, phone_e164: str, code: str) -> bool: ...


class FakeOTP:
    """Development and test provider.

    Accepts a fixed code and never touches the network, so nobody burns real
    WhatsApp message credits running the test suite.
    """

    name = "fake"

    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    async def send(self, phone_e164: str, channel: str) -> None:
        self.sent.append((phone_e164, channel))

    async def verify(self, phone_e164: str, code: str) -> bool:
        return code == DEV_CODE


_instance: OTPProvider | None = None


def get_otp() -> OTPProvider:
    global _instance
    if _instance is None:
        settings = get_settings()
        if settings.otp_provider == "fake":
            _instance = FakeOTP()
        else:  # pragma: no cover - real provider lands in Phase 3
            raise NotImplementedError(
                f"OTP provider '{settings.otp_provider}' is not implemented yet. "
                "OTP provider selection is PIP B6; implementation is "
                "PIP Task 3.2."
            )
    return _instance


def reset_otp(provider: OTPProvider | None = None) -> None:
    global _instance
    _instance = provider
