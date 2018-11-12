from typing import Any, Callable, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.urls.resolvers import URLResolver


def convert_exception_to_response(get_response: Callable) -> Callable: ...
def response_for_exception(
    request: WSGIRequest, exc: Exception
) -> HttpResponse: ...
def get_exception_response(
    request: WSGIRequest,
    resolver: URLResolver,
    status_code: int,
    exception: Exception,
    sender: None = ...,
) -> HttpResponse: ...
def handle_uncaught_exception(request: Any, resolver: Any, exc_info: Any): ...