from base64 import b64decode
from io import BytesIO
from re import search
from typing import List

from PyPDF2 import PdfFileReader

from src.Domain.DTO.PdfFileDto import PdfFileDto
from src.Domain.DTO.PdfFilesDto import PdfFilesDto
from src.Domain.Exception.FilterFileException import FilterFileException


class FilterFiles:

    def filter(self, pdf_files: PdfFilesDto) -> List[PdfFileDto]:
        """
        Receives a list of PDF files, returns a filtered list based on keywords.
        The keywords must match the content of the PDF. If no PDF matches, returns an empty list.

        :param pdf_files: A list of PDFs.
        :return: A list with filtered PDFs or an empty list.
        """
        try:
            filtered_files = []
            keywords = pdf_files.keywords

            for file_data in pdf_files.files:
                pdf_file = PdfFileReader(BytesIO(b64decode(file_data.file)))

                if self.__word_match(keywords, pdf_file):
                    filtered_files.append(PdfFileDto(file_data.file_id, file_data.file))
            return filtered_files

        except Exception as e:
            raise FilterFileException(e.args[0])

    def __word_match(self, keywords: list, pdf_file: PdfFileReader) -> bool:
        for index in range(0, pdf_file.getNumPages()):
            return self.__search_keyword(keywords, pdf_file.getPage(index).extractText())
        return False

    def __search_keyword(self, keywords: list, page_content: str) -> bool:
        for keyword in keywords:
            if search(keyword, page_content):
                return True
        return False
