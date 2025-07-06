from agents.infra_agent import provision_vm
from agents.config_agent import apply_config
from agents.test_agent import test_config

def handle_intent(intent_path):
    import json
    with open(intent_path) as f:
        intent = json.load(f)
    
    vm_count = intent.get("vm_count", 1)
    base_name = intent.get("vm_name_prefix", "mesh-vm")

    for i in range(vm_count):
        name = f"{base_name}-{i}"
        provision_vm(name)
        apply_config(name)
        test_config(name)

    print("[OrchestratorAgent] 🎉 All tasks completed")
