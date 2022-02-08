import os
import asyncio
from nextcord.ext import commands
import logging
from dotenv import load_dotenv




def main():
    client = commands.Bot(command_prefix='$')


    logging.basicConfig(level=logging.INFO)
    logging.debug("Logging!")


    #Import environment vars from the stupid .env file
    load_dotenv("./TOKEN.env")
    # Get the token variable.
    TOKEN = os.getenv('CLIENT_TOKEN')


    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")


    #Loads All Cogs
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")


    @client.command()
    async def reaquire(ctx):
        for folder in os.listdir("modules"):
            try:
                if os.path.exists(os.path.join("modules", folder, "cog.py")):
                    client.reload_extension(f"modules.{folder}.cog")
            except commands.errors.ExtensionNotLoaded:
                continue

        for folder in os.listdir("modules"):
            try:
                if os.path.exists(os.path.join("modules", folder, "cog.py")):
                    client.load_extension(f"modules.{folder}.cog")
            except commands.errors.ExtensionAlreadyLoaded:
                continue

    client.run(TOKEN)


if __name__ == '__main__':
    main()