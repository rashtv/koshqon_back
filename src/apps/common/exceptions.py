from typing import Optional, Union, List, Dict

from rest_framework.exceptions import (
    APIException,
    status,
)


class BaseBadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(
        self,
        detail: Optional[Union[List, Dict, str]] = None,
        code: Optional[Union[str, int]] = None,
    ) -> None:
        super().__init__(detail=detail, code=code)
        if isinstance(self.default_detail, dict):
            self.detail = self.default_detail


class BaseNotFound(BaseBadRequest):
    status_code = status.HTTP_404_NOT_FOUND



