import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


# Load environment variables from .env file
load_dotenv()

# Get environment variables
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Store OAuth2 flow objects for each user
flows = {}


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


auth_url = "https://localhost:8080/v1/api/authenticate"


@bot.command()
async def verify(ctx):
    """
    Sends an authentication URL to the user for verification.

    Args:
        ctx: The context object representing the current state of the bot.
        auth_url: The URL for authentication.

    Returns:
        A string indicating the status or result of the operation.
    """
    try:
        # Send user-friendly message with authentication link
        message = (
            "Please authenticate by clicking the link below:\n"
            f"[Authentication Link]({auth_url})"
        )
        await ctx.send(message)
        return "Verification sent"
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


bot.run(DISCORD_BOT_TOKEN)
