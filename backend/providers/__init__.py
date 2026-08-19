"""Provider adapters.

Every external service sits behind an interface here. Swapping the LLM or the
OTP vendor must touch one adapter and its tests, and nothing in ``services/`` or
``engine/`` — this is the mitigation for PRD risk R5.
"""

from providers.llm import LLMProvider, get_llm
from providers.otp import OTPProvider, get_otp

__all__ = ["LLMProvider", "OTPProvider", "get_llm", "get_otp"]
