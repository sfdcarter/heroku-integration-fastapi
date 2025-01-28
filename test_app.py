from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from heroku_fastapi import sample_header

from .app import app

client = TestClient(app)


@pytest.fixture()
def mocked_simplesf():
    with patch("heroku_fastapi.Salesforce"):
        result = MagicMock()
        yield result


def test_cctx_header(mocked_simplesf):
    response = client.post(
        "/accounts",
        headers={
            "x-client-context": sample_header(),
            "x-request-id": "00DKc000002f2DhMAI-7cdbb76b-b9d8-4fe9-802e-dc9b0a737bc2",
        },
    )
    assert response.status_code == 200
