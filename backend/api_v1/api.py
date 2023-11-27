from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

# api.add_router("/events/", events_router)


@api.get("/")
def home_page(request):
    return {"message": "hello world"}


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
