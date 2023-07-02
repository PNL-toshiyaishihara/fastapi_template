import sys
import time
import json
from typing import Callable
from datetime import datetime
from logging import getLogger, StreamHandler, DEBUG

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = getLogger(__name__)
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        before = time.time()
        response: Response = await call_next(request)
        duration = round(time.time() - before, 4)

        record = {}
        time_local = datetime.fromtimestamp(before)
        record["time_local"] = time_local.strftime("%Y/%m/%d %H:%M:%S%Z")
        if await request.body():
            record["request_body"] = (await request.body()).decode("utf-8")
        record["request_headers"] = {
            k.decode("utf-8"): v.decode("utf-8") for (k, v) in request.headers.raw
        }
        record["remote_addr"] = request.client.host
        record["request_uri"] = request.url.path
        record["request_method"] = request.method
        record["request_time"] = str(duration)
        record["status"] = response.status_code
        logger.info(json.dumps(record))
        return response
