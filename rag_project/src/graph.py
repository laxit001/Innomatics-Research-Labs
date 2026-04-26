from langgraph.graph import StateGraph
from src.retriever import get_retriever
from src.generator import generate_answer

retriever = get_retriever()
def process_node(state):
    query = state["query"]

    docs = retriever.invoke(query)

    if not docs:
        return {
            "query": query,
            "context": "",
            "answer": "No relevant information found.",
            "confidence": 0.2
        }

    context = "\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, query)

    confidence = min(1.0, len(context) / 1000)

    return {
        "query": query,
        "context": context,
        "answer": answer,
        "confidence": confidence
    }

def route_node(state):
    if state["confidence"] < 0.5:
        return "hitl"
    return "output"

def output_node(state):
    print("\n✅ AI Response:\n")
    return {"final_answer": state["answer"]}

def hitl_node(state):
    print("\n⚠️ Escalating to Human (HITL)...\n")
    human_response = input("Enter human response: ")
    return {"final_answer": human_response}

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("process", process_node)
    graph.add_node("output", output_node)
    graph.add_node("hitl", hitl_node)

    graph.set_entry_point("process")

    graph.add_conditional_edges(
        "process",
        route_node,
        {
            "output": "output",
            "hitl": "hitl"
        }
    )

    graph.set_finish_point("output")

    return graph.compile()