import base64
import json
from typing import Annotated

from fastapi import Depends, Header
from simple_salesforce import Salesforce

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

class ClientUserContext(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    username: str = Field()
    user_id: str = Field()

class ClientContextModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)
    request_id: str = Field()
    access_token: str = Field()
    api_version: str = Field()
    namespace: str = Field()
    organization_id: str = Field(alias="orgId")
    org_url: str = Field(alias="orgDomainUrl")
    user_context: ClientUserContext = Field()
    

def client_context(x_client_context: Annotated[str | None, Header(include_in_schema=False)] = None):
    return ClientContextModel(**json.loads(base64.b64decode(x_client_context)))


ClientContext = Annotated[ClientContextModel, Depends(client_context)]


def default_connection(client: ClientContext):
    return Salesforce(
        instance_url=client.organization_id, session_id=client.access_token
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
