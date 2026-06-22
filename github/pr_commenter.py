import requests

from github.github_auth import (
    generate_installation_token
)


def post_pr_comment(
    repo_name,
    pr_number,
    review
):

    token = (
        generate_installation_token()
    )

    url = (
        f"https://api.github.com/repos/"
        f"{repo_name}/issues/"
        f"{pr_number}/comments"
    )

    headers = {
        "Authorization":
        f"token {token}",

        "Accept":
        "application/vnd.github+json"
    }

    body = {
        "body":
        f"## AI Code Review\n\n{review}"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    response.raise_for_status()