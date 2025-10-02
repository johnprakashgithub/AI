import subprocess

def test_config(vm_name):
    cmd = f"multipass exec {vm_name} -- test -f /tmp/hello.txt"
    result = subprocess.run(cmd, shell=True)
    assert result.returncode == 0, f"Test failed on {vm_name}"

