from config_agent import apply_config
from test_agent import test_config
def orchestrate():
    vms = ["test-vm-0", "test-vm-1"]
    for vm in vms:
        apply_config(vm)
        test_config(vm)
    print("✅ All VMs configured and tested.")

orchestrate()

