from flask import Response, request
from flask_restful import Resource

from src.Domain.DTO.PdfFilesDto import PdfFilesDto
from src.Domain.Exception.FilterFileException import FilterFileException
from src.Infrastructure.CrossCutting.Http.StatusHttp import StatusHttp
from src.Infrastructure.CrossCutting.Response.ResponseApi import ResponseApi
from src.Service.FilterFiles import FilterFiles


class PostFileHandler(Resource):

    def __init__(self):
        self.__filter_files = FilterFiles()

    def post(self) -> Response:
        try:
            result = self.__filter_files.filter(PdfFilesDto(request.json))
            return ResponseApi(result, StatusHttp.OK).response()
        except FilterFileException as e:
            return ResponseApi(e.get_message(), e.get_code()).response()
        except Exception as e:
            return ResponseApi(e.args).response()
