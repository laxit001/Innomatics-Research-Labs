from transformers import pipeline

llm = pipeline(
    "text-generation",
    model="google/flan-t5-large",
    device=-1
)

def generate_answer(context, query):
    prompt = f"""
    You are a customer support assistant.

    Use ONLY the context below to answer.
    If answer not found, say "I don't know".

    Context:
    {context}

    Question:
    {query}
    """

    response = llm(
        prompt,
        max_length=200,
        do_sample=False
    )

    return response[0]["generated_text"]