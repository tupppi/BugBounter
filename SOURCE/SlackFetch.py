from os import environ
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# slack messanger
def slackFetch(slackChan,slackMSG):
  environ["?????"] = ""
  client = WebClient(token=environ['SLACK_BOT_TOKEN'])
  
  try:
    response = client.chat_postMessage(channel=slackChan, text=slackMSG)
  except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    print(f"Got an error: {e.response['error']}")