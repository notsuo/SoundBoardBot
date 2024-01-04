import discord
from discord.ext import commands
import os
from asyncio import sleep
from keep_alive import keep_alive

TOKEN = os.getenv("Sound_Board_Bot_TOKEN")


class SoundBoardBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        super().__init__(command_prefix="/", case_insensitive=True, help_command=None, intents=intents)

    async def on_ready(self):
        print("Boot")
        await bot.change_presence(activity=discord.Game("Python"))  # Pythonをプレイ中


class SoundBoard1(discord.ui.View):

    @discord.ui.button(label="くしゃみ出そう！", style=discord.ButtonStyle.blurple)
    async def sound1(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/sneeze.wav"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="吸い込むな！！！", style=discord.ButtonStyle.blurple, custom_id="doNotSuck")
    async def sound2(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/doNotSuck.wav"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="Bだいぶアツいよ！", style=discord.ButtonStyle.blurple)
    async def sound3(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/Bだいぶアツいよ！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="GreatDensuke頭悪い！", style=discord.ButtonStyle.blurple)
    async def sound4(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/GreatDensuke頭悪い！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="あっっぶねー", style=discord.ButtonStyle.blurple)
    async def sound5(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/あっっぶねー.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="いったすぎ痛すぎ", style=discord.ButtonStyle.blurple)
    async def sound6(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/いったすぎ痛すぎ.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="うぉああああ", style=discord.ButtonStyle.blurple)
    async def sound7(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/うぉああああ.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="うわぁぁぁぁ！！！（殺害）", style=discord.ButtonStyle.blurple)
    async def sound8(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/うわぁぁぁぁ（殺害）.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="裏いるらららら", style=discord.ButtonStyle.blurple)
    async def sound9(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/え！裏いるらららら.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="きっっしょあの太い", style=discord.ButtonStyle.blurple)
    async def sound10(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/きっっしょあの太い.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="きっっしょコイツwうわぁぁぁぁ！！！（殺害）", style=discord.ButtonStyle.blurple)
    async def sound11(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/きっっしょコイツwうわぁぁぁぁ（殺害）.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="このレイナ速い！うっっ！", style=discord.ButtonStyle.blurple)
    async def sound12(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/このレイナ速い、うっっ！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="そういうことだぁ！！！", style=discord.ButtonStyle.blurple)
    async def sound13(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/そういうことだぁ！！！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="なんでだよ（犯人声）", style=discord.ButtonStyle.blurple)
    async def sound14(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/なんでだよ（犯人声）.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="なんで当たってんだよ！！！", style=discord.ButtonStyle.blurple)
    async def sound15(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/なんで当たってんだよ！！！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="なんで？！やめろよ！！！", style=discord.ButtonStyle.blurple)
    async def sound16(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/なんで？！やめろよ！！！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="びんびーん", style=discord.ButtonStyle.blurple)
    async def sound17(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/びんびーん.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="まじでかーー！！！", style=discord.ButtonStyle.blurple)
    async def sound18(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/まじでかーー！！！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="やばいってやばい！！！", style=discord.ButtonStyle.blurple)
    async def sound19(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/やばいってやばい！！！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="カバーカバーカバー！", style=discord.ButtonStyle.blurple)
    async def sound21(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/カバーカバーカバー！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="ッヘﾔｯ", style=discord.ButtonStyle.blurple)
    async def sound22(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/ッヘﾔｯ.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="ナイスー", style=discord.ButtonStyle.blurple)
    async def sound23(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/ナイスー.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="一緒に遊ぼう、どうｓ...サイファー、サイファーミッドね", style=discord.ButtonStyle.blurple)
    async def sound24(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/一緒に遊ぼう、どうｓ、、、サイファー、サイファーミッドね.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="強いねぇ～ぼく（死亡）", style=discord.ButtonStyle.blurple)
    async def sound25(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/強いねぇ～ぼく（死亡）.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)


class SoundBoard2(discord.ui.View):
    @discord.ui.button(label="急ぎすぎ急ぎすぎオーディンかよお前！", style=discord.ButtonStyle.blurple)
    async def sound26(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/急ぎすぎ急ぎすぎオーディンかよお前！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="接着するよ", style=discord.ButtonStyle.blurple)
    async def sound27(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/接着するよ.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="本当だからだぁ！", style=discord.ButtonStyle.blurple)
    async def sound28(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/本当だからだぁ！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="本当のこと言って何が悪いんだこの馬鹿！", style=discord.ButtonStyle.blurple)
    async def sound29(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/本当のこと言って何が悪いんだこの馬鹿！.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="来いよ", style=discord.ButtonStyle.blurple)
    async def sound30(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/来いよ.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="死ぬってwww死ぬwww", style=discord.ButtonStyle.blurple)
    async def sound31(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/死ぬってwww死ぬwww.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="逃げたい逃げたいwwwやばい死にたくないwww", style=discord.ButtonStyle.blurple)
    async def sound32(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/逃げたい逃げたいwwwやばい死にたくないwww.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="電車の中では静かにしてください", style=discord.ButtonStyle.blurple)
    async def sound33(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/電車の中では静かにしてください.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

    @discord.ui.button(label="ｓサイファーいるよ！ほらほらほら（殺害）", style=discord.ButtonStyle.blurple)
    async def sound34(self, interaction: discord.Interaction, button: discord.ui.Button):
        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/ｓサイファーいるよ！ほらほらほら（殺害）.mp3"))
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)


class Ultimate(discord.ui.View):
    @discord.ui.button(label="逃げたほうがいいかもね♪", style=discord.ButtonStyle.blurple, custom_id="youShouldRun")
    async def you_should_run(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("再生しています。このメッセージは自動的に削除されます。", delete_after=1)

        for member in interaction.guild.voice_client.channel.members:
            if member.bot:
                continue
            print(member.name)

            await interaction.channel.send(member.mention)

        interaction.guild.voice_client.play(discord.FFmpegPCMAudio("SoundResource/youShouldRun.wav"))
        while interaction.guild.voice_client.is_playing():
            await sleep(0.1)
        await interaction.guild.voice_client.disconnect()
        for member in interaction.channel.members:
            await member.move_to(None)


bot = SoundBoardBot()


async def send_menu(ctx: commands.Context):
    await ctx.send("メニュー", view=SoundBoard1())
    await ctx.send(view=SoundBoard2())


@bot.command()
async def sbb(ctx: commands.Context):
    if ctx.message.author.bot:
        return

    await send_menu(ctx)
    await ctx.message.author.voice.channel.connect()


@bot.command()
async def menu(ctx: commands.Context):
    if ctx.message.author.bot:
        return

    await send_menu(ctx)


@bot.command()
async def ult(ctx: commands.Context):
    if ctx.message.author.bot:
        return

    await ctx.send("Ult", view=Ultimate())
    await ctx.message.author.voice.channel.connect()

keep_alive()
bot.run(TOKEN)
