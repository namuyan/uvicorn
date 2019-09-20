try:
    from .auto import auto_loop_setup
except Exception:
    auto_loop_setup = None

try:
    from .asyncio import asyncio_setup
except Exception:
    asyncio_setup = None

try:
    from .uvloop import uvloop_setup
except Exception:
    uvloop_setup = None


LOOP_SETUPS = {
    "auto": auto_loop_setup,
    "asyncio": asyncio_setup,
    "uvloop": uvloop_setup,
}


__all__ = [
    "LOOP_SETUPS",
]
