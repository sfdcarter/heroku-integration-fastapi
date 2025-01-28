from fastapi import FastAPI

from heroku_fastapi import DefaultConnection, ClientContextDep

app = FastAPI(title="Heroku Integration App")


@app.post("/accounts")
async def list_accounts(sf: DefaultConnection) -> dict[str, str]:
    query_result = sf.query("SELECT Id,Name FROM Account LIMIT 10")
    return {record["Id"]: record["Name"] for record in query_result["records"]}

@app.post("/info")
async def info(client: ClientContextDep) -> dict[str,str]:
    return {"username":client["userContext"]["username"]}