from graph import build_graph
from config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aurum")

logger.info("Invoking graph with goal: %s", settings.target_gain)

def run():
    graph = build_graph()
    graph.invoke({"goal": settings.target_gain})

if __name__ == "__main__":
    run()
