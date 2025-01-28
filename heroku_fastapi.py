import base64
import json
from typing import Annotated

from fastapi import Depends, Header
from simple_salesforce import Salesforce


def xlient_context(x_client_context: Annotated[str | None, Header()] = None):
    return json.loads(base64.b64decode(x_client_context))


ClientContextDep = Annotated[dict, Depends(xlient_context)]


def default_connection(client: ClientContextDep):
    return Salesforce(
        instance_url=client["orgDomainUrl"], session_id=client["accessToken"]
    )


DefaultConnection = Annotated[Salesforce, Depends(default_connection)]


def sample_header():
    structure = {
        "requestId": "00DKc000002f2DhMAI-7cdbb76b-b9d8-4fe9-802e-dc9b0a737bc2",
        "accessToken": "123456",
        "apiVersion": "61.0",
        "namespace": "",
        "orgId": "00DKc000002f2DhMAI",
        "orgDomainUrl": "https://cancun.my.salesforce.com",
        "userContext": {"userId": "00530000003xqAb", "username": "robot@cancun.net"},
    }
    return base64.b64encode(json.dumps(structure).encode("ascii"))
