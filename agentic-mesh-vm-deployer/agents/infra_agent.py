import subprocess

def provision_vm(name="vm-default"):
    print(f"[InfraAgent] Launching VM: {name}")
    cmd = f"multipass launch --name {name} --mem 1G --disk 5G --cpus 1"
    subprocess.run(cmd, shell=True)
