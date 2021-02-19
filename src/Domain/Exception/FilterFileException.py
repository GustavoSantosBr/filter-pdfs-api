from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp


class FilterFileException(Exception):

    def __init__(self, message: str):
        self.__message = message
        super().__init__(self.__message)

    def get_message(self) -> str:
        return f"Não foi possível filtrar o arquivo. Detalhamento do erro: {self.__message}"

    def get_code(self) -> int:
        return StatusHttp.INTERNAL_SERVER_ERROR
