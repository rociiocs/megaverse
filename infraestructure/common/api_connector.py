import time
from typing import Optional

import requests
from requests import Response


class ApiConnector:
    def post(
            self,
            url: str,
            data: dict = None,
            json: Optional[dict] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> Response:

        response = requests.post(url=url, data=data, json=json, headers=headers, params=params)
        response.raise_for_status()
        return response

    def post_retry(
            self,
            url: str,
            data: dict = None,
            json: Optional[dict] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None,
            max_retries: int = 5
    ) -> Response:
        retries = 0

        while retries < max_retries:
            response = requests.post(url=url, data=data, json=json, headers=headers, params=params)

            if response.status_code != 429:
                return response

            retry_after = int(response.headers.get("Retry-After", "5"))
            print(f"Rate limited (429). Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            retries += 1

        response.raise_for_status()
        return response

    def get(
            self,
            url: str,
            data: dict = None,
            json: Optional[dict] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> Response:
        response = requests.get(url=url, data=data, json=json, params=params, headers=headers)
        response.raise_for_status()
        return response

    def delete(
            self,
            url: str,
            data: dict = None,
            json: Optional[dict] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> Response:
        response = requests.delete(url, data=data, json=json, params=params, headers=headers)
        response.raise_for_status()
        return response

    def delete_retry(
            self,
            url: str,
            data: dict = None,
            json: Optional[dict] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None,
            max_retries: int = 5
    ) -> Response:
        retries = 0

        while retries < max_retries:
            response = requests.delete(url, data=data, json=json, params=params, headers=headers)

            if response.status_code != 429:
                return response

            retry_after = int(response.headers.get("Retry-After", "5"))
            print(f"Rate limited (429). Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            retries += 1

        response.raise_for_status()
        return response
