from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.middleware("http")
async def check_discord_bot(request: Request, call_next):
    # Replace 'Your-Discord-Bot-Identifier' with your bot's unique identifier
    print(request.headers.get("User-Agent"))
    if request.headers.get("User-Agent") == "Your-Discord-Bot-Identifier":
        response = await call_next(request)
        return response
    else:
        raise HTTPException(status_code=403, detail="Access denied")


@app.get("/")
async def root():
    return {"message": "Hello World"}
