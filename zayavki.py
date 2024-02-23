import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from disnake import Embed, Color
import asyncio
from datetime import datetime
import datetime
from disnake import ui
from datetime import datetime, timezone, timedelta
import os
from disnake.ext import commands as discommands
from disnake.ui import TextInput, View
import requests



class MyModal(disnake.ui.Modal):
    def __init__(self, channel_id):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Ваше имя:",
                placeholder="ваня",
                custom_id="имя:",
                style=TextInputStyle.short,
                max_length=30,
            ),
            disnake.ui.TextInput(
                label="Ваш возраст?",
                placeholder="16",
                custom_id="Возраст:",),
            
            disnake.ui.TextInput(
                label="Часовой пояс относительно МСК",
                placeholder="МСК",
                custom_id="Часовой пояс относительно МСК:",
            
            ),

            disnake.ui.TextInput(
                label="Раскажите о себе",
                placeholder="Я общительный и добрый",
                custom_id="о себе:",
                style=TextInputStyle.paragraph,

            ),
            disnake.ui.TextInput(
                label="Почему вы решили стать на эту должность?",
                placeholder="Я хорошо знаю правила сервера",
                custom_id="Почему вы решили стать на эту должность?:",
                style=TextInputStyle.paragraph,
            ),
        ]
        self.channel_id = channel_id
        super().__init__(title="Create Tag", components=components)

    # The callback received when the user input is completed.
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Новая заявка!")

        # Adding information about the user who submitted the application
        embed.add_field(name="От:", value=inter.user.mention, inline=False)

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )



        channel = bot.get_channel(self.channel_id)

        # Отправка информации в канал
        await channel.send(embed=embed)

        # Отправка сообщения пользователю об успешной отправке заявки
        await inter.response.send_message("Заявка успешно отправлена!", ephemeral=True)


class MyModal(disnake.ui.Modal):
    def __init__(self, channel_id):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Ваше имя:",
                placeholder="ваня",
                custom_id="имя:",
                style=TextInputStyle.short,
                max_length=30,
            ),
            disnake.ui.TextInput(
                label="Ваш возраст?",
                placeholder="16",
                custom_id="Возраст:",),
            
            disnake.ui.TextInput(
                label="Часовой пояс относительно МСК",
                placeholder="МСК",
                custom_id="Часовой пояс относительно МСК:",
            
            ),

            disnake.ui.TextInput(
                label="Раскажите о себе",
                placeholder="Я общительный и добрый",
                custom_id="о себе:",
                style=TextInputStyle.paragraph,

            ),
            disnake.ui.TextInput(
                label="Почему вы решили стать на эту должность?",
                placeholder="Я хорошо знаю правила сервера",
                custom_id="Почему вы решили стать на эту должность?:",
                style=TextInputStyle.paragraph,
            ),
        ]
        self.channel_id = channel_id
        super().__init__(title="Create Tag", components=components)

    # The callback received when the user input is completed.
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Новая заявка!")

        # Adding information about the user who submitted the application
        embed.add_field(name="От:", value=inter.user.mention, inline=False)

        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )



        channel = bot.get_channel(self.channel_id)

        # Отправка информации в канал
        await channel.send(embed=embed)

        # Отправка сообщения пользователю об успешной отправке заявки
        await inter.response.send_message("Заявка успешно отправлена!", ephemeral=True)

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), test_guilds=[ВАШ ID СЕРВЕРА])
@bot.event
async def on_ready():
    print('Бот запущен!')

red = 72
green = 61
blue = 139


@bot.command()
async def buttons(ctx):
    allowed_channel_id = 1101472234008219675  # ID канала где будет работать комманда

    if ctx.channel.id != allowed_channel_id:
        return  # Выход из функции, если не в нужном канале
    embed = disnake.Embed(
        title="Открыт набор на стафф сервера",
        description="<@&1101472232431161490> - встречают новичков на сервере и проводят им экскурсию, а также отвечают на все вопросы пользователей.\n"
        "<@&1101472232431161484> - творческие личности отвечающие за мини мероприятия. \n"
        "<@&1143595076757500016> - занимаются продвижением сервера. \n"
        "<@&1101472232431161491> - следят за соблюдением правил сервера в текстовых и голосовых каналах, а также разбирают жалобы от пользователей. \n"
        "\n"
        "> **Что от вас требуется?** \n"
        "Быть готовым уделять серверу 2-3 часа в день \n"
        "16 полных лет \n"
        "Знание и понимание правил сервера и дискорда",
        color=Color.from_rgb(red, green, blue)
    )
    await ctx.send(embed=embed, components=[
        disnake.ui.Button(label="Саппорт", style=disnake.ButtonStyle.primary, custom_id="staff"),
        disnake.ui.Button(label="Креатив ", style=disnake.ButtonStyle.primary, custom_id="creative"),
        disnake.ui.Button(label="SMM manager", style=disnake.ButtonStyle.primary, custom_id="Медиа"),
        disnake.ui.Button(label="Модератор", style=disnake.ButtonStyle.primary, custom_id="Бампер")
    ])


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["staff", "creative", "Медиа", "Бампер"]:
        return

    channel_ids = {
        "staff": 1196515593357107401, #ID канала для заявки на staff
        "creative": 1196524273624416307, #ID канала для заявки на креатив
        "Медиа": 1196548783962607759, #ID канала для заявки на медиа
        "Бампер": 1196548702060412969, #ID канала для заявки на бампер
    }

    modal = MyModal(channel_id=channel_ids[inter.component.custom_id])
    await inter.response.send_modal(modal=modal)
        
verified_count = 0

# Пропишите комманду !buttons в канал который вы указывали 
bot.run("ВАШ TOKEN БОТА")
