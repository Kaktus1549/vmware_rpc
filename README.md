# VMware RPC

VMware RPC is a python script that displays the running virtual machines on discord.

## Installation

You can download .tar.gz/.zip file here: [VMware RPC](https://github.com/Kaktus1549/vmware_rpc/releases/latest)
<br>To unpack the file you can use this commands:

For .tar.gz file:

```bash
tar -xvf vmware_rpc.tar.gz
```

For .zip file:

```bash
unzip vmware_rpc.zip
```


To install dependencies for this script, run the following command:

```bash
pip install -r requirements.txt
```

After running the script for the first time, a config file will be generated. You will need to edit this file to add application ID, path to vmrun and name of VMware workstation (e.g. vmware.exe or vmware-vmx.exe).

Here is an example of the config file:

```json
{
    "application_id": "13223121",
    "vmrun_path": "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmrun.exe",
    "vmware_file": "vmware.exe"
}
```

### Application ID

To get the application ID, you will need to create a discord application. You can do this by going to the [Discord Developer Portal](https://discord.com/developers/applications) and clicking on "New Application". After creating the application, you can find the application ID under the "General Information" tab.
There is also "Rich Presence" tab, you can add images to rich presence. Image keys mean the name of the image.
<br>Example -> image key is here "kali-image"

![example](./images/image_key.png)

## Usage

In order to run the script, you need VMware Workstation running (the script will close himself if VMware Workstation is not running).  <br>
You can run the script by running the following command:

```bash
python main.py
```

The script will every 15 seconds check running virtual machines, if he founds any, he will check if the virtual machine is presented in vms.json file. If not, the script will add the virtual machine to the vms.json file with default image key (kali-image). If the virtual machine is presented in vms.json file, the script will take information from vms.json (e.g. image key, hostname, os that you set) and display it on discord.
If you want edit hostname, os or image key, you have to edit vms.json file in ./settings/. <br>
Here is an example of vms.json:

```json
{
    "default": "default-image",
    "no_vm": "no_vm-image",
    "kali":{
        "hostname": "KaliCTF",
        "os": "Kali Linux",
        "image_key": "kali-image"
    }
}
```
