import configparser
import pickle
from discord_webhook import DiscordWebhook, DiscordEmbed
from work_with_db import DataBase




class DiscordInvites:
    def __init__(self, webhook_url):
        config = configparser.ConfigParser()
        config.read("../settings1.ini")
        self.first_message = None
        self.webhook_url = webhook_url
        self.webhook = DiscordWebhook(url=self.webhook_url)
    def send_first_message(self):
        embed = DiscordEmbed(title='Your Title', description='Webhook content before edit', color='03b2f8')
        self.webhook.add_embed(embed)
        self.first_message = self.webhook.execute()

    def change_message(self, family):
        embed = DiscordEmbed(title='Инвайты на сегодня', color='03b2f8')

        db = DataBase()
        tod_inv = db.get_today_invites(family)
        for inv in tod_inv:
            embed.add_embed_field(name=inv[2],
                                  value=f'**[{inv[0]}]({inv[1]})** `с {inv[3].split("-")[0]} до {inv[3].split("-")[1]}`',
                                  inline=False)
        self.webhook.remove_embeds()

        self.webhook.add_embed(embed)
        # embed.set_footer(text='тугникс лох')
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
    def get_all(self):
        db = DataBase()
        return db.get_all()

if __name__ == '__main__':
    # отправка первого
    d = DiscordInvites('')
    famqs = d.get_all()

    # for id, fam, hook in famqs:
    #     d = DiscordInvites(hook)
    #     d.send_first_message()
    #     with open(f"{fam.lower()}.pkl", "wb") as fp:
    #         pickle.dump(d, fp)
    #     print(id, fam, hook)



    for id, fam, hook in famqs:
        with open(f"{fam.lower()}.pkl", "rb") as fp:
            d = pickle.load(fp)

        d.change_message(fam)


    # d.webhook_url = 'https://discordapp.com/api/webhooks/985930850594086962/pgJEVUEPYQc_NZExg6BQBq5oViyrS7UQEzVA-Y5604evc7jO9wOz57ZDwRY3H2ToR09d'
    # d.send_first_message()
    # with open("phantom.pkl", "wb") as fp:
    #     pickle.dump(d, fp)

    #
    # with open("phantom.pkl", "rb") as fp:
    #     d = pickle.load(fp)
    # d.change_message()
    # with open("invites/db.json", "r", encoding="utf-8") as file:
    #     data = json.load(file)
    # print(data['invites'])