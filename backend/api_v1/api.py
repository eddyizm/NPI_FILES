from django.urls import path
from ninja import NinjaAPI
# from api_v1.api import router as home_router

api = NinjaAPI()

# api.add_router("/events/", events_router)
# api.add_router("/", home_router)

@api.get('/')
def home_page(request):
    return {"message": "hello world"}


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

urlpatterns = [
    path("api_v1/", api.urls),
]

