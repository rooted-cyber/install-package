"""
 ────────────────────────────────────────────────────────
 ✨             DeepSeek Plugin for Ultroid          ✨
 ────────────────────────────────────────────────────────
--->t.me/testingplugin
 🔗 This plugin enables users to interact with the DeepSeek API
    through the Ultroid Telegram userbot.

 🌟 Features:
   - Send prompts to DeepSeek and receive AI-generated responses.
   - Manage chat sessions by clearing and starting new ones.
   - Toggle Thinking Mode and Search Mode to customize responses.
     - **Commands:**
       - `.deep -c`      : Clear and reset the current chat session.
       - `.deep -t`      : Toggle Thinking Mode (enable/disable).
       - `.deep -s`      : Toggle Search Mode (enable/disable).
       - `.deep -st`     : Enable both Thinking Mode and Search Mode.
       - `.deep <prompt>`: Send a prompt to DeepSeek and receive a response.

 👨‍💻 Developed and maintained by:
   Charlie

 🔒 Copyright © 2023 Charlie
    All rights reserved. Unauthorized copying is prohibited.

 ────────────────────────────────────────────────────────

"""

from os import system, remove
from io import BytesIO
import json
import asyncio

try:
    import requests
except ImportError:
    system("pip install -q requests")
    import requests

from . import ultroid_cmd, LOGS

# Constants for command flags
COMMAND_CLEAR_SESSION = "-c"
COMMAND_THINK = "-t"
COMMAND_SEARCH = "-s"
COMMAND_BOTH = "-st"

# Initialize or retrieve chat session data
chat_session_data = {
    "chat_session_id": None,
    "parent_message_id": None,
    "message_increment": 2,
    "search_enabled": False,
    "thinking_enabled": False
}

# Function to create a new chat session
def create_new_chat_session() -> str:
    url = "https://chat.deepseek.com/api/v0/chat_session/create"
    headers = {
        "x-client-platform": "android",
        "x-client-version": "1.0.8",
        "x-client-locale": "en_US",
        "x-rangers-id": "7885738793599816448",
        "user-agent": "DeepSeek/1.0.8 Android/25",
        "authorization": "Bearer 0ToWTUOP7FsY2JQ85zMXb0WsUnam3TVNe55dLXicRmon2l+5SIzmZN4HcsWHYkas",
        "accept": "application/json",
        "accept-charset": "UTF-8",
        "content-type": "application/json",
        "accept-encoding": "gzip"
    }
    data = '{"agent":"chat"}'

    try:
        response = requests.post(url, headers=headers, data=data, timeout=30)
        response.raise_for_status()
        response_json = response.json()
        id_value = response_json["data"]["biz_data"]["id"]
        LOGS.info(f"New chat_session_id created: {id_value}")
        return id_value
    except requests.exceptions.RequestException as e:
        LOGS.warning(f"Failed to create new chat session: {e}", exc_info=True)
        return None

# Initialize chat_session_id on startup if not present
if not chat_session_data["chat_session_id"]:
    chat_session_data["chat_session_id"] = create_new_chat_session()

def get_deep_response(prompt: str) -> str:
    """
    Synchronously fetches a response from the DeepSeek API based on the given prompt.
    Handles cases where the response is blank or indicates no reply by resetting the parent_message_id.
    """
    if not chat_session_data["chat_session_id"]:
        LOGS.warning("No chat_session_id available.")
        return "❌ Error: No chat session available. Please reset the session using `.deep -c`."

    url = 'https://chat.deepseek.com/api/v0/chat/completion'

    headers = {
        'x-ds-pow-response': 'eyJhbGdvcml0aG0iOiJEZWVwU2Vla0hhc2hWMSIsImNoYWxsZW5nZSI6IjY5OTY5M2RhNWU4MjU1NmQwMjY1NmI0NDVhYjdmMjVlNTJhMDFiODA4MzgzZjJjNjJlZTJhZjc4ODJmYmEzOWQiLCJzYWx0IjoiZDUyODRkOGIzYjUzZTE4MTdhMWYiLCJzaWduYXR1cmUiOiJlYTNiNjU3MTI1OGE2ZDg5OGIwODFjNWJkYzdjMjRmNjJlMjBlYTRmZDY5YmUwOWM2NmI5ZjAxNDViMDNkNWFiIiwiYW5zd2VyIjoyODMyMywidGFyZ2V0X3BhdGgiOiIvYXBpL3YwL2NoYXQvY29tcGxldGlvbiJ9',
        'x-client-platform': 'android',
        'x-client-version': '1.0.8',
        'x-client-locale': 'en_US',
        'x-rangers-id': '7885738793599816448',
        'User-Agent': 'DeepSeek/1.0.8 Android/25',
        'Authorization': 'Bearer 0ToWTUOP7FsY2JQ85zMXb0WsUnam3TVNe55dLXicRmon2l+5SIzmZN4HcsWHYkas',
        'Accept': 'application/json',
        'Accept-Charset': 'UTF-8',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip',
    }

    data = {
        "chat_session_id": chat_session_data["chat_session_id"],
        "parent_message_id": chat_session_data["parent_message_id"],
        "prompt": prompt,
        "ref_file_ids": [],
        "thinking_enabled": chat_session_data["thinking_enabled"],
        "search_enabled": chat_session_data["search_enabled"],
        "legacy_format": True
    }

    try:
        response = requests.post(url, headers=headers, json=data, stream=True, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        LOGS.warning(f"DeepSeek API request failed: {e}", exc_info=True)
        return f"❌ Error: Unable to fetch response from DeepSeek API. {e}"

    complete_response = ""
    try:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    json_data = decoded_line[6:]  # Remove "data: " prefix
                    if json_data.strip() == "[DONE]":
                        break
                    try:
                        parsed_data = json.loads(json_data)
                        if "choices" in parsed_data and len(parsed_data["choices"]) > 0:
                            delta = parsed_data["choices"][0].get("delta", {})
                            content = delta.get("content", "")
                            complete_response += content
                    except json.JSONDecodeError:
                        continue
    except Exception as e:
        LOGS.warning(f"Error processing DeepSeek API response: {e}", exc_info=True)
        return f"❌ Error: An issue occurred while processing the response. {e}"

    # If response indicates no reply, reset parent_message_id and retry
    if "I didn't receive any response. Please try again." in complete_response or not complete_response.strip():
        LOGS.warning("Received no response. Resetting parent_message_id and retrying.")
        chat_session_data["parent_message_id"] = None
        # Retry fetching the response
        data["parent_message_id"] = None
        try:
            response = requests.post(url, headers=headers, json=data, stream=True, timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            LOGS.warning(f"DeepSeek API retry request failed: {e}", exc_info=True)
            return f"❌ Error: Unable to fetch response from DeepSeek API on retry. {e}"

        complete_response = ""
        try:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith("data: "):
                        json_data = decoded_line[6:]  # Remove "data: " prefix
                        if json_data.strip() == "[DONE]":
                            break
                        try:
                            parsed_data = json.loads(json_data)
                            if "choices" in parsed_data and len(parsed_data["choices"]) > 0:
                                delta = parsed_data["choices"][0].get("delta", {})
                                content = delta.get("content", "")
                                complete_response += content
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            LOGS.warning(f"Error processing DeepSeek API retry response: {e}", exc_info=True)
            return f"❌ Error: An issue occurred while processing the retry response. {e}"

        # Add [X] to indicate chat history interruption
        if complete_response.strip():
            complete_response = "[X] " + complete_response

    # Update parent_message_id if response was successful
    if chat_session_data["parent_message_id"] is None and not complete_response.startswith("[X]"):
        chat_session_data["parent_message_id"] = 2
    elif not complete_response.startswith("[X]"):
        chat_session_data["parent_message_id"] += 3

    return complete_response or "🤔 I didn't receive any response. Please try again."

@ultroid_cmd(pattern="dp(?:\s|$)(.*)")
async def deep_command_handler(e):
    """
    Handles the `.deep` command with subcommands:
      - `.deep -c`  : Clear and reset the current chat session.
      - `.deep -t`  : Toggle Thinking Mode (enable/disable).
      - `.deep -s`  : Toggle Search Mode (enable/disable).
      - `.deep -st` : Enable both Thinking Mode and Search Mode.
      - `.deep <prompt>`: Send a prompt to DeepSeek and receive a response.
    """
    args = e.pattern_match.group(1).strip()
    reply = await e.get_reply_message()

    # Handle subcommands
    if args.startswith(COMMAND_CLEAR_SESSION):
        # Clear chat session
        await e.eor("🧹 Clearing the current chat session...")
        new_session_id = create_new_chat_session()
        if new_session_id:
            chat_session_data["chat_session_id"] = new_session_id
            chat_session_data["parent_message_id"] = None
            chat_session_data["search_enabled"] = False
            chat_session_data["thinking_enabled"] = False
            return await e.edit("✅ Chat session has been reset.")
        else:
            return await e.edit("❌ Failed to reset chat session.")

    elif args.startswith(COMMAND_BOTH):
        # Enable both thinking and search
        chat_session_data["thinking_enabled"] = True
        chat_session_data["search_enabled"] = True
        # Changed from e.edit to e.reply
        return await e.reply("🧠🔍 Both Thinking Mode and Search Mode have been **enabled** for your queries.")

    elif args.startswith(COMMAND_THINK):
        # Toggle Thinking Mode
        chat_session_data["thinking_enabled"] = not chat_session_data["thinking_enabled"]
        if chat_session_data["thinking_enabled"]:
            # If enabled, disable search mode to prevent conflicts
            chat_session_data["search_enabled"] = False
            response = "🧠 **Thinking Mode has been enabled** for your queries."
        else:
            response = "🧠 **Thinking Mode has been disabled** for your queries."
        # Changed from e.edit to e.reply
        return await e.reply(response)

    elif args.startswith(COMMAND_SEARCH):
        # Toggle Search Mode
        chat_session_data["search_enabled"] = not chat_session_data["search_enabled"]
        if chat_session_data["search_enabled"]:
            # If enabled, disable thinking mode to prevent conflicts
            chat_session_data["thinking_enabled"] = False
            response = "🔍 **Search Mode has been enabled** for your queries."
        else:
            response = "🔍 **Search Mode has been disabled** for your queries."
        # Changed from e.edit to e.reply
        return await e.reply(response)

    else:
        # Regular deep command to process the prompt
        if not args:
            if reply and reply.text:
                args = reply.text
        if not args:
            return await e.eor("❌ Please provide a prompt for DeepSeek.\n\n**Usage:** `.deep <your prompt>` or reply to a message with `.deep`.")

        status_message = await e.eor("🔄 Processing your request with DeepSeek...")

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            # If no current event loop, create a new one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        try:
            response_text = await loop.run_in_executor(None, get_deep_response, args)
            if not response_text:
                response_text = "🤔 I didn't receive any response. Please try again."
        except Exception as exc:
            LOGS.warning(exc, exc_info=True)
            return await status_message.edit(f"❌ An unexpected error occurred: {exc}")
        else:
            if len(response_text) < 4095:
                #answer = f"**DeepSeek Response:**\n\n{response_text}"
                answer = f"**Deepseek**\n\n**Sawal**\n\n`{args}`\n\n**response** 👇\n\n**{response_text}**"
                return await status_message.edit(answer,parse_mode="md")
            else:
                with BytesIO(response_text.encode()) as file:
                    file.name = "deepseek_response.txt"
                    await e.client.send_file(
                        e.chat_id, file, caption="**DeepSeek Response:**", reply_to=e.reply_to_msg_id
                    )
                await status_message.delete()
