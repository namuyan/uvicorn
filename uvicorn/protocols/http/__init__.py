try:
    from .auto import AutoHTTPProtocol
except Exception:
    AutoHTTPProtocol = None

try:
    from .h11_impl import H11Protocol
except Exception:
    H11Protocol = None

try:
    from .httptools_impl import HttpToolsProtocol
except Exception:
    HttpToolsProtocol = None


HTTP_PROTOCOLS = {
    "auto": AutoHTTPProtocol,
    "h11": H11Protocol,
    "httptools": HttpToolsProtocol,
}


__all__ = [
    "HTTP_PROTOCOLS",
]
