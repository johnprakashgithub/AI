def check_policy(vm_spec):
    # Simple example: block GPUs on weekdays
    from datetime import datetime
    if "gpu" in vm_spec.get("type", "").lower():
        if datetime.now().weekday() < 5:
            return False
    return True
