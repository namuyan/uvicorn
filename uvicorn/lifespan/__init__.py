from .on import LifespanOn
from .off import LifespanOff


LIFESPAN = {
    "auto": LifespanOn,
    "on": LifespanOn,
    "off": LifespanOff,
}


__all__ = [
    "LIFESPAN",
]
