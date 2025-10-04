from config import CONFIG
from langgraph.graph import StateGraph
from graph.nodes.TrelloFetcher import TrelloFetcher
from graph.nodes.StatusSummarizer import StatusSummarizer
from graph.nodes.EmailSender import EmailSender
from graph.nodes.MemoryStore import MemoryStore

# Initialize nodes using config
trello_node = TrelloFetcher(
    api_key=CONFIG["trello_api_key"],
    token=CONFIG["trello_token"],
    board_id=CONFIG["trello_board_id"]
)

summarizer_node = StatusSummarizer(
    openai_api_key=CONFIG["openai_api_key"],
    model="gpt-4"
)

email_node = EmailSender(
    smtp_host=CONFIG["smtp_host"],
    smtp_port=CONFIG["smtp_port"],
    smtp_user=CONFIG["smtp_user"],
    smtp_password=CONFIG["smtp_password"],
    from_email=CONFIG["email_from"],
    to_email=CONFIG["email_to"]
)

memory_node = MemoryStore(storage_path="memory_logs.json")

# Build LangGraph
graph = StateGraph()
graph.add_node("TrelloFetcher", trello_node)
graph.add_node("StatusSummarizer", summarizer_node)
graph.add_node("EmailSender", email_node)
graph.add_node("MemoryStore", memory_node)

graph.set_entry_point("TrelloFetcher")
graph.add_edge("TrelloFetcher", "StatusSummarizer")
graph.add_edge("StatusSummarizer", "EmailSender")
graph.add_edge("StatusSummarizer", "MemoryStore")

mira_graph = graph.compile()
