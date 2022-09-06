"""Github models."""

from pydantic import BaseModel


class GitHubWebhookPayload(BaseModel):
    """Github payload model."""

    # Full spec: https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#push

    ref: str

    before: str
    after: str

    # TODO Build proper models
    repository: dict
    head_commit: dict

    pusher: dict
    sender: dict

    # TODO Implement other attributes
