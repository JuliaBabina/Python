from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Дратути {update.effective_user.first_name}')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/sub\n/mult\n/div\n')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # sum 123 455
    x = float(items[1])
    y = float(items[2])


    await update.message.reply_text(f'{x} + {y} = {round((x+y),2)}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  
    x = float(items[1])
    y = float(items[2])


    await update.message.reply_text(f'{x} - {y} = {round((x-y),2)}')


async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  
    x = float(items[1])
    y = float(items[2])


    await update.message.reply_text(f'{x} * {y} = {round((x*y),2)}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  
    x = float(items[1])
    y = float(items[2])


    await update.message.reply_text(f'{x} / {y} = {round((x/y),2)}')

