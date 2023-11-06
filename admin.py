import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6756382486:AAHUsWFitebat6oBdXY9CgfwVF3zkZTcwkA'

# Telegram API endpoint for getting updates
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'

# Send a GET request to the API endpoint
response = requests.get(url)

# Parse the JSON response to extract chat ID
data = response.json()
chat_id = data['result'][0]['message']['chat']['id']

print(f"Admin's Chat ID: {chat_id}")