from typing import List

from src.Domain.DTO.PdfFileDto import PdfFileDto


class PdfFilesDto:

    def __init__(self, data: dict):
        self.__keywords = data.get("keywords")
        self.__files = data.get("files")

    @property
    def keywords(self) -> list:
        keywords = []

        for keyword in self.__keywords:
            if not isinstance(keyword, str):
                keyword = str(keyword)
            keywords.append(keyword.strip())
        return keywords

    @property
    def files(self) -> List[PdfFileDto]:
        files = []

        for file in self.__files:
            files.append(PdfFileDto(file.get("file_id"), file.get("file")))
        return files
