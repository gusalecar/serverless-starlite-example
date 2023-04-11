import os

from mangum import Mangum
from litestar import Router, Litestar, get

from db import get_data


@get("/{report_id:int}")
async def get_report(report_id: int) -> dict[str, str]:
    return {"message": f"Report {report_id} and {get_data()}"}


reports_router = Router("/reports", route_handlers=[get_report])
app = None


def handler(event, context):
    global app
    if not app:
        app = Litestar([reports_router])
    path = os.environ["BASE_PATH"]
    asgi_handler = Mangum(app, lifespan="off", api_gateway_base_path=path)
    return asgi_handler(event, context)
