import os, sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchFrameException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import logging
import re
import time
import random
import string
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/telegram", methods=["POST"])
async def telegram_webhook():
    update = Update.de_json(request.get_json(), application.bot)
    await application.process_update(update)
    return {"status": "ok"}
    
@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "running"}), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "timestamp": time.time()}), 200

@app.route("/wakeup", methods=["GET"])
def wakeup():
    logger.info("Сервис пробуждён!")
    return jsonify({"status": "awake", "timestamp": time.time()}), 200

def open():
 time.sleep(60)
 options = webdriver.ChromeOptions()
 options.add_argument("--headless")
 options.add_argument("--disable-blink-features=AutomationControlled")
 options.add_argument("--no-sandbox")
 options.add_argument("--disable-dev-shm-usage")
 options.add_argument("--disable-gpu")
 options.add_argument("--disable-extensions")
 options.add_argument("--disable-infobars")
 options.add_argument("--start-maximized")
 options.add_argument("--window-size=1920,1080")
 options.add_argument("--ignore-certificate-errors")
 options.add_argument("--allow-running-insecure-content")
 options.add_argument("--disable-web-security")
 options.add_argument("--disable-features=IsolateOrigins,site-per-process")
 user_agent = (
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
 )
 options.add_argument(f"user-agent={user_agent}")
 options.add_experimental_option('useAutomationExtension', False)
 options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
 options.add_experimental_option('excludeSwitches', ['enable-logging'])
 
 while True:
  drivery = webdriver.Chrome(options=options)
  drivery.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  url='https://zap_1.onrender.com/'
  drivery.get(url)
  time.sleep(30)
  drivery.quit()
  time.sleep(600)

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

from threading import Thread
flask_thread = Thread(target=run_flask, daemon=True)
flask_thread.start()

open()