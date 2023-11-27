# schemas.py
from typing import Optional

from ninja import Schema


class DownloadURLIn(Schema):
    file_name: str
    created_by: Optional[str]
    url: str
