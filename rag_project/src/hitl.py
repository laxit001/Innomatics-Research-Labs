from __future__ import annotations

import logging


LOGGER = logging.getLogger(__name__)


def get_human_response(query: str, context: str) -> str:
    print("\nEscalation triggered. A human support agent is needed.")
    print(f"Customer query: {query}")
    if context.strip():
        preview = context[:500]
        print(f"Retrieved context preview: {preview}")
    human_answer = input("Human agent response: ").strip()
    LOGGER.info("Human response captured for escalated query")
    return human_answer or "A human agent will follow up shortly."
