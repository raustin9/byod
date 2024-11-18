from __future__ import annotations
from _auto import auto

from fastapi.middleware.cors import CORSMiddleware

# App
app = auto.fastapi.FastAPI()

# static
app.mount(
    '/static',
    auto.fastapi.staticfiles.StaticFiles(
        directory=(
            auto.pathlib.Path(__file__).parent / 'static'
        ),
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index(
    *,
    request: auto.fastapi.Request
):
    return auto.fastapi.Response(
        content='Hello World',
        status_code=200,
        media_type='text/plain'
    )

async def run_server():
    config = auto.uvicorn.Config(
        "server:app",
        port=4971,
        host='0.0.0.0',
    )
    server = auto.uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    auto.asyncio.run(run_server())