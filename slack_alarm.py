import requests
import re
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
import telegram

#env var
tg_token = os.environ['TelegramToken']
tg_chat_id = os.environ['TelegramChatId']

line_token = os.environ['LineToken']
line_user_id = os.environ['LineUserId']

im_tools = os.environ['ImTools']

def tg_push(push_message):
	tg_bot = telegram.Bot(token=tg_token)
	tg_bot.send_message(chat_id=tg_chat_id, text=push_message)

def line_push(push_message):
	line_bot_api = LineBotApi(line_token)
	line_bot_api.push_message(line_user_id, 
	    TextSendMessage(text=push_message))
# select IM tool
def select_tool(tool_name,msg):
	if tool_name == 'tg':
		tg_push(msg)
	elif tool_name == 'line':
		line_push(msg)
	else:
		tg_push(msg)
		line_push(msg)

def lambda_handler(event, context):
	print('Lambda run')
	slack_status_url = 'https://status.slack.com/'
	# define RegEx pattern
	issues_pattern = re.compile(r'issues\saffecting\sall\sworkspaces')
	outage_pattern = re.compile(r'outage|Outage')

	# request slack page and get text for parsing
	slack_status_req = requests.get(slack_status_url)
	slack_content = slack_status_req.text
	
	# RegEx search
	re_isssues = re.search(issues_pattern, slack_content)
	re_outage = re.search(outage_pattern, slack_content)

	if re_isssues != None and re_outage != None:
		select_tool(im_tools,'Slack is down now and affect all workspaces.\nDetails check https://status.slack.com/.\nPlease use line for communitcation.')
		print('Slack Down.')
	else:
		select_tool(im_tools,'Slack is good now.')
		print('Slack Good.')