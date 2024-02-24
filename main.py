import asyncio
from typing import AsyncIterable
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

class StreamModel:
    stream: AsyncIterable[str]

    class Config:
        schema_alias = "StreamModel"

async def get_stream_of_data() -> AsyncIterable[str]:
    for _ in range(30):
        await asyncio.sleep(1) # これに相当する箇所がブロッキングしている？
        yield "A"

async def get_stream() -> AsyncIterable[str]:
    # データストリームからデータを非同期的に取得
    stream = get_stream_of_data()
    async for data in stream:
        yield data

@app.get("/")
async def get_stream_api():
    """AsyncIterrableでStreamを返却するAPI"""

    stream = get_stream()
    return StreamingResponse(content=stream)

