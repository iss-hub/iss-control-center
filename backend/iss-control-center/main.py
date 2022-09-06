"""Server to manage project state."""

from fastapi import FastAPI

from .models.github import GitHubWebhookPayload


app = FastAPI()  # noqa: W001

# TODO Add data storage


@app.get("/")
def read_root():
    """Index page."""

    return {"Message": "Change me later"}


# TODO Add dummy handler for new issues
# TODO Add dummy handler for removed issues

# TODO Manage issues for GitHub
# - Create tickets
# - Close tickets
# - List issues

# TODO Add registration for project
# TODO Add registration for engineer

# TODO Think on how to accept payments
# TODO Think on giving rewards

# TODO Handle GitHub webhook


@app.post("/webhook/github", status_code=201)
def webhook_github(payload: GitHubWebhookPayload):
    """Processing GitHub webhook."""

    # TODO Send update event to message bus, so it could clone repo and check for diffs

    (payload.dict().keys())

    return True
