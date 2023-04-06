import os

from mangum import Mangum
from starlite import Router, Starlite, get

from db import get_data


@get("/{team_id:int}")
async def get_team(team_id: int) -> dict[str, str]:
    return {"message": f"Team {team_id} and {get_data()}"}

# The router is required to locally execute
teams_router = Router("/teams", route_handlers=[get_team])
app = None

# You should adapt this handler to your needs
def handler(event, context):
    global app
    if not app:
        app = Starlite([teams_router])
    path = os.environ["BASE_PATH"]
    asgi_handler = Mangum(app, lifespan="off", api_gateway_base_path=path)
    return asgi_handler(event, context)
