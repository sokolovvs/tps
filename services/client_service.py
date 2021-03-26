class ClientService:

    @staticmethod
    def check_access(request: dict) -> None:
        """
        :param request: dict
        :raises Exception
        :return: None
        """
        # success if user have an active subscription and a rate limit is not reach
        pass
