from enum import Enum


class StatusCode(Enum):
    # HTTP Status Codes
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    GONE = 410
    PAYLOAD_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

    # WebSocket Status Codes
    WS_NORMAL_CLOSURE = 1000
    WS_GOING_AWAY = 1001
    WS_PROTOCOL_ERROR = 1002
    WS_UNSUPPORTED_DATA = 1003
    WS_NO_STATUS_RCVD = 1005
    WS_ABNORMAL_CLOSURE = 1006
    WS_INVALID_FRAME_PAYLOAD_DATA = 1007
    WS_POLICY_VIOLATION = 1008
    WS_MESSAGE_TOO_BIG = 1009
    WS_MANDATORY_EXT = 1010
    WS_INTERNAL_ERROR = 1011
    WS_SERVICE_RESTART = 1012
    WS_TRY_AGAIN_LATER = 1013
    WS_BAD_GATEWAY = 1014
    WS_TLS_HANDSHAKE = 1015
