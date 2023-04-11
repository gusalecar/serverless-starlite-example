from litestar import Litestar
from reports.app import reports_router
from teams.app import teams_router


app = Litestar([reports_router, teams_router])
