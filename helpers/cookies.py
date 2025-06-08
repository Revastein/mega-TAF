import json

from helpers.utils import get_file_abs_path

_ALLOWED_FIELDS = {
    "name",
    "value",
    "domain",
    "path",
}


def setup_cookies_from_file(driver, json_path="components/cookies.json"):
    file_path = get_file_abs_path(json_path)
    with file_path.open(encoding="utf-8") as f:
        raw = json.load(f)

    cookies = raw if isinstance(raw, list) else [raw]

    for ck in cookies:
        payload = {k: ck[k] for k in _ALLOWED_FIELDS if k in ck}
        driver.add_cookie(payload)

    driver.refresh()
