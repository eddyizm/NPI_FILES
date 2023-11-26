from ninja import NinjaAPI
from api_v1.api import router as home_router
# from events.api import router as events_router

api = NinjaAPI()

# api.add_router("/events/", events_router)
api.add_router("/", home_router)
