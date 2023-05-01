import asyncio

import openai

from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


async def mp3_to_text(filename: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None,
                                      _sync_mp3_to_text,
                                      filename)


async def get_response_chatgpt(promt: list) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None,
                                      _sync_create_chat_completion,
                                      promt)


def _sync_mp3_to_text(filename: str) -> str:

    with open(filename, 'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript.text


def _sync_create_chat_completion(promt: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=promt
    )
    return resp['choices'][0]['message']['content']
