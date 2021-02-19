# Filter PDFs API

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/GustavoSantosBr/)
[![Minimum Python Version](https://img.shields.io/badge/python-%5E3.9.1-blue)](https://www.python.org)

* [Introdução](#Introdução)
* [Instalação](#Instalação)
* [Endpoints](#Endpoints)
* [Observações](#Observações)

## Introdução

Filtra uma lista de arquivos PDFs que estão em base64. A filtragem ocorre ao procurar as palavras-chave informadas na
requisição, dentro do conteúdo dos PDFs. Se uma palavra for encontrada, o PDF em questão é adicionado à lista de
retorno.

## Instalação

- Abra seu terminal, navegue até o diretório de sua preferência, e em seguida execute:
  ```bash
  > git clone https://github.com/GustavoSantosBr/filter-pdfs-api.git
  ```

- Navegue até a pasta do projeto utilizando:
  ```bash
  > cd cd {seudiretorio}
  ```

- Em seguida, execute o comando abaixo para dar início ao contêiner do projeto:
  ```bash
  > docker-compose up -d
  ```

- Se necessário entrar no bash do contêiner, execute:
  ```bash
  > docker exec -it filter_api bash
  ```

## Endpoints

**POST** `/files`

Filtra uma lista de PDFs com base em uma lista de palavras-chave.

- **Exemplo:**
    - Request
       ```json
          {
                "keywords": [
                    "xxxxxxx",
                    "xxxxx xxxx"
                ],
                "files": [
                    {
                        "file_id": 1,
                        "file": "JVBERi0xLjUKJeLjz9MKNCAwIG9iago8PC9GaWx0ZXIvRmxhdGVEZWNvZGUvTGVuZ3RoIDc4MjAvTGVuZ3R
                                oMSAzNjM2OD4+c3RyZWFtCnic7X0LdFNHluCt9/Tx3zLYYBDBZYTBIMXyhwAmdJCwZezY2I4swCYhSJaeLRlZUiQ
                                5jhMyhmHZJCaZkMk/3b1hdvtsJ72Z8CB9OiabLHQv001ON9skmf7t6Z6w3elAepPGzSSZ2ZCgvVXvSZbNZzt9ts
                                /MnPOqXFW3bt26/6N+dpKPv7P73AJsWAQgHB2KDw2KyIgCwtgDA+NBg..."
                    },
                    {
                        "file_id": 2,
                        "file": "JVBERi0xLjUKJeLjz9MKNCAwIG9iago8PC9GaWx0ZXIvRmxhdGVEZWNvZGUvTGVuZ3RoIDc4MjAvTGVuZ3R
                                oMSAzNjM2OD4+c3RyZWFtCnic7X0LdFNHluCt9/Tx3zLYYBDBZYTBIMXyhwAmdJCwZezY2I4swCYhSJaeLRlZUiQ
                                5jhMyhmHZJCaZkMk/3b1hdvtsJ72Z8CB9OiabLHQv001ON9skmf7t6Z6w3elAepPGzSSZ2ZCgvVXvSZbNZzt9ts
                                /MnPOqXFW3bt26/6N+dpKPv7P73AJsWAQgHB2KDw2KyIgCwtgDA+NBg..."
                    }
                ]
         }
      ```
    - Response
       ```json
          {
              "data": [
                  {
                      "file_id": 1,
                      "file": "JVBERi0xLjUKJeLjz9MKNCAwIG9iago8PC9GaWx0ZXIvRmxhdGVEZWNvZGUvTGVuZ3RoIDc4MjAvTGVuZ3R
                                oMSAzNjM2OD4+c3RyZWFtCnic7X0LdFNHluCt9/Tx3zLYYBDBZYTBIMXyhwAmdJCwZezY2I4swCYhSJaeLRlZUiQ
                                5jhMyhmHZJCaZkMk/3b1hdvtsJ72Z8CB9OiabLHQv001ON9skmf7t6Z6w3elAepPGzSSZ2ZCgvVXvSZbNZzt9ts
                                /MnPOqXFW3bt26/6N+dpKPv7P73AJsWAQgHB2KDw2KyIgCwtgDA+NBg..."
                  }
              ]
          }
       ```

      ou (Se nenhuma palavra-chave for encontrada)

       ```json
          {
              "data": []
          }
       ```

## Observações

- PDFs com codificações personalizadas podem não conseguir ser lidos corretamente. 