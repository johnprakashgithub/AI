registry = {}

def register(agent_name, capabilities):
    registry[agent_name] = capabilities
    print(f"[Registry] Registered {agent_name} with {capabilities}")
