from django.urls import path
from ninja import Router

router = Router()

# api.add_router("/events/", events_router)


@router.get("/")
def home_page(request):
    return {"message": "hello world"}


@router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
