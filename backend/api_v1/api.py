from ninja import Field, Query, Router
from typing import List
from .models import NpiRawData
from .schemas.query_filters import NPISearchFilter

router = Router()


@router.get("/")
def home_page(request):
    return {"message": "hello world"}


@router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@router.get("/providers", response=List[NPISearchFilter])
def list_providers(request, filters: NPISearchFilter = Query(...)):
    # TODO this table needs to be refactored to smaller subset.
    npi_providers = NpiRawData.objects.filter(filters.get_filter_expression())
    return npi_providers
