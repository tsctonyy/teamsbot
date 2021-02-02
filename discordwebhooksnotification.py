from discord_webhooks import DiscordWebhooks


webhook_url = "Deine URL"

def send_msg(notificationtitle, message):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
   
    webhook.set_footer(text='Microsoft Team Bots')

    webhook.set_content(title=notificationtitle,
                          description=message)

    webhook.send()

