import subprocess

def apply_config(vm_name):
    cmd = f"multipass exec {vm_name} -- bash -c 'echo Hello > /tmp/hello.txt'"
    subprocess.run(cmd, shell=True)

apply_config("test-vm-0")
apply_config("test-vm-1")

