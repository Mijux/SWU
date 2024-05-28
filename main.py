#!/usr/bin/env python3

from dotenv import load_dotenv
from flask import Flask, request
from os import getenv
from os.path import join
from requests import get as rget

from utils.deploy import deploy_tar_gz
from utils.exceptions import GithubException, SignatureException, DeployException
from utils.logger import setup_logger, get_logger
from utils.signature import verify_signature

app = Flask(__name__)

load_dotenv()
setup_logger()

GITHUB_ACCESS_TOKEN = getenv("GITHUB_TOKEN")
GITHUB_OWNER = getenv("GITHUB_OWNER")
GITHUB_REPO = getenv("GITHUB_REPO")
GITHUB_WEBHOOK_SECRET = getenv("GITHUB_WEBHOOK_SECRET")

GITHUB_LATEST_URL = join(
    "https://api.github.com/repos", GITHUB_OWNER, GITHUB_REPO, "releases/latest"
)

WEB_ROOT = getenv("WEB_ROOT")
WEB_DEPLOY_ENDPOINT = getenv("WEB_DEPLOY_ENDPOINT")


@app.route(WEB_DEPLOY_ENDPOINT, methods=["POST"])
def update_from_github():
    if request.is_json:
        payload = request.get_json()
    else:
        get_logger().warning("Payload must be json")
        return "Payload must be json", 403

    try:
        if payload.get("action") == "created":
            verify_signature(
                request.data,
                GITHUB_WEBHOOK_SECRET,
                request.headers.get("X-Hub-Signature-256", default=None),
            )

            # Retrieve the latest release uploaded on github to get the asset id
            headers = {
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
            }
            latest_release = rget(GITHUB_LATEST_URL, headers=headers)

            if latest_release.status_code != 200:
                get_logger().error("Can't retrieve latest release")
                get_logger().debug(latest_release.content)
                raise GithubException("Can't retrieve latest release")

            asset_id = str(latest_release.json().get("assets")[0].get("id"))

            # Retrieve the asset file
            headers = {
                "Accept": "application/octet-stream",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
            }
            url = join(
                "https://api.github.com/repos",
                GITHUB_OWNER,
                GITHUB_REPO,
                "releases/assets",
                asset_id,
            )

            release_file = rget(url, headers=headers)

            if release_file.status_code != 200:
                get_logger().error("Can't download asset file from latest release")
                get_logger().debug(release_file.content)
                raise GithubException("Can't download asset file from latest release")

            return deploy_tar_gz(WEB_ROOT, release_file.content)

    except GithubException as e:
        return e.args[0], e.error_code
    except SignatureException as e:
        return e.args[0], e.error_code
    except DeployException as e:
        return e.args[0], e.error_code


if __name__ == "__main__":
    app.run(debug=False, host="localhost", port=8000)
