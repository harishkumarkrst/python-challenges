import urllib.request
import urllib.parse
import urllib.error
import json


def make_get_request(url, params=None):

    if params:
        query_string = urllib.parse.urlencode(params)
        url = f"{url}?{query_string}"

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            return json.loads(body)

    except (urllib.error.HTTPError, urllib.error.URLError):
        return None


def make_post_request(url, data):

    body = json.dumps(data).encode("utf-8")

    headers = {
        "Content-Type": "application/json"
    }

    request = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(
                response.read().decode("utf-8")
            )

    except (urllib.error.HTTPError, urllib.error.URLError):
        return None


class APIClient:

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

        self.headers.setdefault(
            "Content-Type",
            "application/json"
        )


    def set_header(self, key, value):
        self.headers[key] = value


    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        return make_get_request(url, params)


    def post(self, endpoint, data):
        url = self.base_url + endpoint
        return make_post_request(url, data)