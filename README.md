# slack-alarm
serverless slack alarm push to line/telegram

## Prepare
Get telegram info. for parameters
* tg token
* tg chat id

Get line info. for parameters
* line token
* line user id

Select IM tool for parameter "ImTools"
* tg
* line
* all

## Build
Select code deployment method:

1. Use src/lambda.zip
2. Package the python code

Use src/lambda.zip
Direct use the src/lambda.zip

Package the python code
```
pip3 install python-telegram-bot -t .
pip3 install line-bot-sdk -t .
zip -r lambda.zip .
```

## Use AWS SAM
```
aws cloudformation package --template-file template.yaml --s3-bucket bucket_name --output-template-file packaged-template.yaml
aws cloudformation deploy --template-file packaged-template.yaml --stack-name stack_name --parameter-overrides TelegramToken=tg_token LineToken=line_token TelegramChatId=tg_chat_id ImTools=all LineUserId=line_user_id --capabilities CAPABILITY_IAM
```