from pypresence import Presence
from time import time, sleep
import json

try:
    # Load config
    print("Trying to load config...")
    try:
        with open("settings.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        
        # If config file not found, create it
        print("Config file not found!")
        print("Creating config file...")
        config ={
        "application_id": "ID_HERE"
        }
        with open("settings.json", "w") as f:
            json.dump(config, f, indent=4)
        print("Config file created!")
        print("Please fill in the config file and restart the program!")
        exit()
    except Exception as e:
        
        # If error while loading config file
        print("Error while loading config file!")
        print(e)
        exit()

    if config["application_id"] == "ID_HERE":
        print("Please fill in the config file and restart the program!")
        exit()
    else:
        rpc = Presence(config["application_id"])
    print("Trying to connect to Discord...")
    try:
        rpc.connect()
    except Exception as e:
        print("Error while connecting to Discord!")
        print(e)
        exit()
    print("Connected to Discord!")
    start_time = time()

    def rpc_update(vm_hostname, vm_os, start_time, image_key):
        rpc.update(
            state="OS: " + vm_os,
            details="Hostname: " + vm_hostname,
            large_image=image_key,
            large_text="Virtualizing...",
            start=start_time
        )

    while True:
        rpc_update("KaliCTF", "Kali Linux", start_time, "kali-image")
        sleep(15)
except KeyboardInterrupt:
    rpc.close()
    print("\nDisconnected from Discord!")
    print("Exiting...")
    exit()
except Exception as e:
    print("\nError!")
    print(e)
    exit()
