from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from aiohttp import web

from config import CONFIG
from tools import LOG

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    LOG.info(f"Message: {message.text}")
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


async def on_startup(bot: Bot) -> None:
    # If you have a self-signed SSL certificate, then you will need to send a public
    # certificate to Telegram
    await bot.set_webhook(f"{CONFIG.BASE_WEBHOOK_URL}{CONFIG.WEBHOOK_PATH}")
    LOG.debug("Bot started")


def main() -> None:
    dp = Dispatcher()
    dp.include_router(router=router)

    dp.startup.register(on_startup)

    bot = Bot(token=CONFIG.TOKEN)

    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=CONFIG.WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=CONFIG.WEB_SERVER_HOST, port=CONFIG.WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
