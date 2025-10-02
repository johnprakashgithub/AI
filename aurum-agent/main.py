from graph import build_graph
from config import settings

def run():
    graph = build_graph()
    graph.invoke({"goal": settings.target_gain})

if __name__ == "__main__":
    run()
