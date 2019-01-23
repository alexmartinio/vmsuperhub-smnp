import os

from dotenv import load_dotenv

load_dotenv(override=True)

ROUTER_IP = os.environ.get("router_ip")
USERNAME = os.environ.get("username")
PASSWORD = os.environ.get("password")
