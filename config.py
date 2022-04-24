from os import environ 

BOT_TOKEN = environ.get("BOT_TOKEN", "")
WEBHOOK_HOST = environ.get("WEBHOOK_HOST", "") # "your_domain.com"
WEBHOOK_PATH = environ.get("WEBHOOK_PATH", "/demo") # "/web_app_example"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBAPP_HOST = environ.get("WEBAPP_HOST", "0.0.0.0")
WEBAPP_PORT = int(environ.get("WEBAPP_PORT", 8000))
