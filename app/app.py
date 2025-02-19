from fastapi import FastAPI

from .heroku_fastapi import DefaultConnection, ClientContext

app = FastAPI(title="Heroku Integration App")
app.openapi_version = "3.0.0" # n.b. this does NOT affect the actual schema generation, see README.md

@app.post("/accounts", operation_id="listAccounts")
async def list_accounts(sf: DefaultConnection) -> dict[str, str]:
    query_result = sf.query("SELECT Id,Name FROM Account LIMIT 10")
    return {record["Id"]: record["Name"] for record in query_result["records"]}

@app.post("/info", operation_id="userInfo", )
async def info(client: ClientContext) -> dict[str,str]:
    return {"username": client.user_context.username}

@app.post("/options", operation_id="ClimateOptions")
async def opts():
    return {"suggestions":[{"heat pump":2000}, {"basement insulation": 1000}]}