import requests
from collections import deque
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
from . import ultroid_cmd, LOGS, fast_download, check_filename
from io import BytesIO

API_URL = "https://mpzxsmlptc4kfw5qw2h6nat6iu0hvxiw.lambda-url.us-east-2.on.aws/process"
GPT_CHAT_HISTORY = deque(maxlen=30)
TELEGRAM_CHAR_LIMIT = 4096
API_KEY = "sk-78dac3dbe3ee47f38dd5c9f1407bffb3"
#API_KEY = "sk-proj-hZn6l5KJd6n8kLJzHzyAT3BlbkFJitztuVQn17ElVhezrFyI"

def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
    }

@ultroid_cmd(pattern="db(?: (.+)|$)")
async def generate_code(event):
    pb = "•••••••••••••••••••••"
    reply_message = await event.get_reply_message()
    query = event.pattern_match.group(1)

    if not query and reply_message:
        query = reply_message.message
    if not query:
        return await event.eor("Please provide a prompt or reply to a message for the Buddy API call.")

    if query == "-c":
        GPT_CHAT_HISTORY.clear()
        return await event.eor("__Cleared Buddy Chat History!__", time=6)

    payload = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.9,
        "messages": list(GPT_CHAT_HISTORY) + [{"role": "user", "content": query}]
    }

    msg = await event.eor(f"Generating response for: {query[:128]} ...")
    GPT_CHAT_HISTORY.append({"role": "user", "content": query})

    try:
        response = requests.post(API_URL, headers=get_headers(), json=payload)
        response.raise_for_status()
        data = response.json()

        generated_response = data["choices"][0]["message"]["content"]
        GPT_CHAT_HISTORY.append({"role": "assistant", "content": generated_response})

        full_message = f"{pb}{pb}\n**BUDDY**\n{pb}{pb}\n\n**Query:**\n~ `{query}`\n\n**Response:**\n~ **{generated_response}**"

        if len(full_message) > TELEGRAM_CHAR_LIMIT:
            with BytesIO(full_message.encode()) as file:
                file.name = "generated_response.txt"
                await event.client.send_file(
                    event.chat_id, file, caption="The query and response were too long, sent as a file.", reply_to=event.reply_to_msg_id
                )
            await msg.delete()
        else:
            await msg.edit(full_message,parse_mode="md")
    except Exception as exc:
        LOGS.error(f"Error generating response: {exc}")
        GPT_CHAT_HISTORY.pop()
        await msg.edit(f"Failed to generate response: {str(exc)}")

# Script crafted by Charlie (t.me/@chillyyyyyyyy)
