import sys
import os

# 🔥 Add project root to Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.graph import build_graph

app = build_graph()

while True:
    query = input("\nAsk your question: ")
    result = app.invoke({"query": query})
    print("\n💬 Answer:", result["final_answer"])