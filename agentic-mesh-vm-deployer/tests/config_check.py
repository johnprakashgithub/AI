import subprocess

def validate(name):
    cmd = f"multipass exec {name} -- cat /tmp/config_status.txt"
    result = subprocess.run(cmd, shell=True)
    if result.returncode == 0:
        print(f"[Test] {name} ✅ Valid")
    else:
        print(f"[Test] {name} ❌ Config missing")
