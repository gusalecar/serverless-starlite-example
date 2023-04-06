from starlite import Starlite
from reports.app import reports_router
from teams.app import teams_router


app = Starlite([reports_router, teams_router])
