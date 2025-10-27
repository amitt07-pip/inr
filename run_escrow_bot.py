"""
Run PagaL Escrow Bot only
"""
import asyncio
import sys
import types
import os

if sys.version_info >= (3, 13):
    sys.modules["imghdr"] = types.ModuleType("imghdr")

def main():
    escrow_token = os.getenv("ESCROW_BOT_TOKEN")
    if not escrow_token:
        print("❌ ERROR: ESCROW_BOT_TOKEN not set!")
        sys.exit(1)
    
    print("✅ PagaL Escrow Bot (@PagaLEscrowBot) - Starting...")
    
    import escrow_bot
    from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ChatMemberHandler
    
    app = ApplicationBuilder().token(escrow_token).build()
    
    app.add_handler(CommandHandler("start", escrow_bot.start_command))
    app.add_handler(CommandHandler("menu", escrow_bot.menu_command))
    app.add_handler(CommandHandler("escrow", escrow_bot.escrow_command))
    app.add_handler(CommandHandler("dispute", escrow_bot.dispute_command))
    app.add_handler(CommandHandler("dd", escrow_bot.dd_command))
    app.add_handler(CommandHandler("buyer", escrow_bot.buyer_command))
    app.add_handler(CommandHandler("seller", escrow_bot.seller_command))
    app.add_handler(CommandHandler("token", escrow_bot.token_command))
    app.add_handler(CommandHandler("deposit", escrow_bot.deposit_command))
    app.add_handler(CommandHandler("balance", escrow_bot.balance_command))
    app.add_handler(CommandHandler("blacklist", escrow_bot.blacklist_command))
    app.add_handler(CallbackQueryHandler(escrow_bot.button_callback))
    app.add_handler(ChatMemberHandler(escrow_bot.track_chat_members, ChatMemberHandler.CHAT_MEMBER))
    
    async def post_init(application):
        asyncio.create_task(escrow_bot.monitor_deposits(application))
    
    app.post_init = post_init
    
    print("✅ PagaL Escrow Bot is running...")
    print("✅ Bot is now polling for updates...")
    
    app.run_polling()

if __name__ == "__main__":
    main()
