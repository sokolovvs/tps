import requests
from requests.exceptions import HTTPError
from exceptions.access_denied_exception import AccessDeniedException
from settings import get_parameter_by_key


class ClientService:

    @staticmethod
    def check_access(request) -> None:
        """
        :param request: dict
        :raises Exception|AccessDeniedException
        :return: None
        """
        from app import app

        try:
            uri = get_parameter_by_key("ENDPOINT_ADD_REQUEST")
            response = requests.post(uri,
                                     json={"text": request["text"]},
                                     headers={"tps-public-id": request["public_id"], "tps-secret": request["secret"]})
            response.raise_for_status()

        except HTTPError as http_err:
            app.logger.error("Service getting the response " + str(http_err))
            raise AccessDeniedException("Access denied")
        except Exception as err:
            app.logger.error("Service getting the response " + str(err))
            raise Exception("Internal server error")
