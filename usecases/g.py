from claude_api import Client
cookie =' sessionKey=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; intercom-device-id-lupk8zyo=b7514ddf-eb6a-4fd5-9950-fc988056aa43; intercom-session-lupk8zyo=ZlRuYm05MEJZNDc1OERCRVZ6Y1d2aURmUWt4dHo4b1NCUHl4SGg4NW5nRWRRdGtTQzlOWWl4a1pvSXNtOVVPby0tZDNpV1dVZTRxbnhFbzFSWWgzQ3hIdz09--a45b5044ec1596ac2dbffcd4a41f115230b8aa51; __cf_bm=OrSLgeavrTKQOAljQjiXakJJ8qbXVq8dVRSNySWFQ44-1690121636-0-AYBqR0nyXxol8TI328D0FM5RDCuKFx80opsMxO87gciTIZdjhvAHBMegV5miYbNrp+y0U9ONADtqhNkRKRZYTYI='
 

claude_api = Client(cookie)

new_chat = claude_api.create_new_chat()
conversation_id = new_chat['uuid']
print(conversation_id)

prompt = "Hello, Claude!"
response = claude_api.send_message(prompt, conversation_id)
print(response)