import configparser
import pickle
from discord_webhook import DiscordWebhook, DiscordEmbed
from work_with_db import DataBase




class DiscordInvites:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../settings.ini")
        self.first_message = None
        self.webhook_url = config["settings"]["hook"]
        self.webhook = DiscordWebhook(url=self.webhook_url)

    def send_first_message(self):
        embed = DiscordEmbed(title='Your Title', description='Webhook content before edit', color='03b2f8')
        self.webhook.add_embed(embed)
        self.first_message = self.webhook.execute()

    def change_message(self):
        embed = DiscordEmbed(title='Инвайты на сегодня', color='03b2f8')

        db = DataBase()
        tod_inv = db.get_today_invites()
        for inv in tod_inv:
            embed.add_embed_field(name=inv[2],
                                  value=f'**[{inv[0]}]({inv[1]})** *({inv[4]} LVL)* `с {inv[3].split("-")[0]} до {inv[3].split("-")[1]}`',
                                  inline=False)
        self.webhook.remove_embeds()

        self.webhook.add_embed(embed)
        embed.set_footer(text='тугникс лох')
        updated = self.webhook.edit(self.first_message)

    def send_stats(self):
        embed = DiscordEmbed(title='Инвайты на сегодня', color='03b2f8')
        db = DataBase()
        tod_inv = db.get_today_invites()
        for inv in tod_inv:
            embed.add_embed_field(name=inv[2],
                                  value=f'**[{inv[0]}]({inv[1]})** *({inv[4]} LVL)* `с {inv[3].split("-")[0]} до {inv[3].split("-")[1]}`',
                                  inline=False)
        # embed.add_embed_field(name='🌵 LaMesa', value='**[RM](https://discord.gg/8BZt6USJea)** *(2 LVL)* с 14:00 до 23:00',
        #                       inline=False)

        self.webhook.add_embed(embed)
        self.webhook.execute()


if __name__ == '__main__':
    # d = DiscordInvites()
    # d.send_first_message()
    # d.send_stats()

    # with open("test.pkl", "wb") as fp:
    #     pickle.dump(d, fp)
    with open("test.pkl", "rb") as fp:
        d = pickle.load(fp)
    d.change_message()
    # with open("invites/db.json", "r", encoding="utf-8") as file:
    #     data = json.load(file)
    # print(data['invites'])