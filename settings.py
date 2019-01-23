import os

from dotenv import load_dotenv

ROUTER_IP = None
USERNAME = None
PASSWORD = None


def load_settings():
    load_dotenv(override=True)
    global ROUTER_IP, USERNAME, PASSWORD
    ROUTER_IP = os.environ.get("router_ip")
    USERNAME = os.environ.get("username")
    PASSWORD = os.environ.get("password")


def create_settings():
    if ROUTER_IP is None:
        print("Creating new .env file for storing settings.")
        password = input("Please enter your Superhub password: ")

        with open(".env", "a") as file:
            lines = [
                "# Superhub 3 IP address",
                "router_ip = '192.168.0.1'", "",
                "# Superhub 3 uses the username 'admin'",
                "username = 'admin'",
                "password = '{}'".format(password)]
            for line in lines:
                file.write(line + '\n')

            load_settings()


load_settings()
create_settings()
