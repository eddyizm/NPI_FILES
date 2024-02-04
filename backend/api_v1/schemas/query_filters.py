from typing import Optional

from ninja import Field
from ninja import Schema, FilterSchema


class NPISearchFilter(FilterSchema):
    npi: Optional[str] = None
    provider_last_name_legal_name_field: Optional[str] = Field(None, q='provider_last_name_legal_name_field__icontains')
    provider_first_name: Optional[str] = Field(None, q='provider_first_name__icontains')
    provider_business_mailing_address_state_name: Optional[str] = Field(None, q='provider_business_mailing_address_state_name__icontains')
    provider_business_mailing_address_postal_code: Optional[str] = Field(None, q='provider_business_mailing_address_postal_code__icontains')


class NotFoundSchema(Schema):
    message: str
