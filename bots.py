# bot.py
from instabot import Bot
import config
import logging

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("Bot started")
    try:
        # Initialize the bot
        bot = Bot()

        # Login using credentials from config.py
        bot.login(username=config.USERNAME, password=config.PASSWORD)

        # Follow users based on some criteria
        users_to_follow = bot.get_users_followers("example_user")
        bot.follow_users(users_to_follow)

        logging.info("Bot finished following users")
    except Exception as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
