from vm_ware import VMWare
from pypresence import Presence
from time import time, sleep
import json, os

if os.path.exists("./config/") == False:
    os.mkdir("./config/")

try:
    # Load config
    print("Trying to load config...")
    try:
        with open("./config/settings.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        
        # If config file not found, create it
        print("Config file not found!")
        print("Creating config file...")
        config ={
        "application_id": "ID_HERE",
        "vmrun_path": "PATH_HERE"
        }
        with open("./config/settings.json", "w") as f:
            json.dump(config, f, indent=4)
        print("Config file created!")
        print("Please fill in the config file and restart the program!")
        exit()
    except Exception as e:
        
        # If error while loading config file
        print("Error while loading config file!")
        print(e)
        exit()

    print("Loading images...")
    try:
        with open("./config/vms.json", "r") as f:
            images = json.load(f)
    except FileNotFoundError:
        images = {}
        with open("./config/vms.json", "w") as f:
            json.dump(images, f, indent=4)
    except Exception as e:
        print("Error while loading images!")
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

    def rpc_update(status, vm_hostname, vm_os, start_time, image_key):
        # Status 1 -> some vm is running
        # Status 2 -> no vm is running
        
        if status == 1:
            if vm_hostname == None:
                detail = "Virtualizing..."
            else:
                detail = "Hostname: " + vm_hostname
            rpc.update(
                state="OS: " + vm_os,
                details=detail,
                large_image=image_key,
                large_text="Virtualizing...",
                start=start_time
            )
        elif status == 2:
            rpc.update(
                state="No VMs running",
                details="I am not virtualizing yet!",
                large_image=images["no_vm"],
                large_text="VMware Workstation Pro",
                start=start_time
            )
        else:
            raise Exception(f"Invalid status: {status}")

    if config["vmrun_path"] == "PATH_HERE":
        print("Please fill in the config file and restart the program!")
        exit()
    vm_instance = VMWare(config["vmrun_path"])
    
    while True:
        status, vm_hostname, vm_os, image_key = vm_instance.process_running_vms()
        rpc_update(status, vm_hostname, vm_os, start_time, image_key)
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
