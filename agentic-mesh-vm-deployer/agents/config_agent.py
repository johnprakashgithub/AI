import subprocess

def apply_config(name):
    print(f"[ConfigAgent] Applying config to {name}")
    cmd = f"multipass exec {name} -- bash -c 'echo configured > /tmp/config_status.txt'"
    subprocess.run(cmd, shell=True)
