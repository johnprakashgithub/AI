import subprocess

def test_config(name):
    print(f"[TestAgent] Verifying config on {name}")
    cmd = f"multipass exec {name} -- test -f /tmp/config_status.txt"
    result = subprocess.run(cmd, shell=True)
    if result.returncode == 0:
        print(f"[TestAgent] ✅ {name} passed")
    else:
        print(f"[TestAgent] ❌ {name} failed")
