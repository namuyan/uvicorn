try:
    from .auto import AutoWebSocketsProtocol
except Exception:
    AutoWebSocketsProtocol = None

try:
    from .websockets_impl import WebSocketProtocol
except Exception:
    WebSocketProtocol = None

try:
    from .wsproto_impl import WSProtocol
except Exception:
    WSProtocol = None


WS_PROTOCOLS = {
    "none": None,
    "auto": AutoWebSocketsProtocol,
    "websockets": WebSocketProtocol,
    "wsproto": WSProtocol,
}


__all__ = [
    "WS_PROTOCOLS",
]
