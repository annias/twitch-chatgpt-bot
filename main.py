from twitchio.ext import commands
from src import responses
import asyncio

async def split_message(ctx, message):
  if len(message) <= 500:
    await ctx.send(message)
  else:
    messages = []
    while len(message) > 0:
      messages.append(message[:500])
      message = message[500:]
    for m in messages:
      await ctx.send(m)
      await asyncio.sleep(0.5)

class Bot(commands.Bot):
  def __init__(self):
    super().__init__(token=,
                     prefix=,
                     initial_channels)

  async def event_ready(self):
    print(f'Logged in as | {self.nick}')

  @commands.command()
  async def ask(self, ctx: commands.Context, *, question: str):
    answer = await responses.handle_response(question)
    await split_message(ctx, f"{ctx.author.mention}. {answer}")

bot = Bot()
bot.run()
