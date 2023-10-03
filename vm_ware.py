import subprocess
import json, os

class VMWare:
    def __init__(self):
        try:
            with open("./config/vms.json", "r") as f:
                vms = json.load(f)
        except FileNotFoundError:
            vms = {}
            with open("./config/vms.json", "w") as f:
                json.dump(vms, f, indent=4)
        except Exception as e:
            raise Exception(f"Error while loading vms.json: {e}")
        self.vms = vms
        self.vmrun_path = r'"C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmrun.exe"'

    def get_running_vms(self):
        try:
            process_output = subprocess.check_output(f"{self.vmrun_path} list", shell=True)
            # splits the output into a list of lines and then removes the path from each line, so that only the VM name is left (e.g. "C:\Users\user\Documents\Virtual Machines\KaliCTF\KaliCTF.vmx" -> "KaliCTF.vmx")
            # skip the first line because it's just the header and remove \r from the end of each line
            return [line.split("\\")[-1].rstrip("\r") for line in process_output.decode().split("\n")[1:] if line != ""]
        except subprocess.CalledProcessError:
            raise Exception("Got CalledProcessError while trying to get running VMs!")
        except Exception as e:
            raise Exception(f"Error while trying to get running VMs: {e}")

    def process_running_vms(self):
        running_vms = self.get_running_vms()
        if len(running_vms) == 0:
            return 2, None, None, None
        newest_vm = running_vms[len(running_vms) - 1]
        if newest_vm not in self.vms:
            self.vms[newest_vm] = {
                "hostname": "",
                "os": newest_vm.split(".")[0],
                "image_key": ""
            }
            with open("./config/vms.json", "w") as f:
                json.dump(self.vms, f, indent=4)
            hostname = None
            os = newest_vm.split(".")[0]
            image_key = self.vms["default"]
        else:
            hostname = self.vms[newest_vm]["hostname"]
            os = self.vms[newest_vm]["os"]
            if self.vms[newest_vm]["image_key"] != "":
                image_key = self.vms[newest_vm]["image_key"]
            else:
                image_key = self.vms["default"]
        return 1, hostname, os, image_key

test = VMWare()
print(test.get_running_vms())
print(test.process_running_vms())