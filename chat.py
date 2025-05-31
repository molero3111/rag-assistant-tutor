import requests
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def get_relevant_context(query, k=4):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])

def send_message_to_model(message, context):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    prompt = (
    "You are a helpful tutor for children and teenagers. "
    "Use the following context from textbooks to help answer the question. "
    "Let's think step by step.\n\n"
    "If the context contains relevant formulas, definitions, or examples, use them to solve the problem, even if the exact answer is not present. "
    "If the context is not helpful in the way that the question is not really about math nor biology, you may answer based on your own knowledge.'\n\n"
    "If the context is not helpful at all, still try to solve their inquiry either with your knowledge or by suggesting another book or resource.'\n\n"
    f"Context:\n{context}\n\nQuestion:\n{message}"
    )
    payload = {
        "model": "mistralai/mathstral-7b-v0.1",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=600)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error communicating with the model: {e}"

def send_message_to_model_with_history(messages):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "mistralai/mathstral-7b-v0.1",
        "messages": messages
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=600)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error communicating with the model: {e}"

def main():
    print("Welcome to the Math Tutor CLI!")
    print("Type 'exit' to end the chat.")
    conversation_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending chat. Goodbye!")
            break
        context = get_relevant_context(user_input)
        # Add previous turns to the messages
        if not conversation_history:
            system_prompt = (
            "You are a helpful tutor for children and teenagers. "
            "Use the following context from textbooks to help answer the question. "
            "Let's think step by step.\n\n"
            "If the context contains relevant formulas, definitions, or examples, use them to solve the problem, even if the exact answer is not present. "
            "If the context is not helpful in the way that the question is not really about math nor biology, you may answer based on your own knowledge.\n\n"
            "If the context is not helpful at all, still try to solve their inquiry either with your knowledge or by suggesting another book or resource.\n\n"
            f"Context:\n{context}\n\nQuestion:\n{user_input}"
            )
            messages = [{"role": "user", "content": system_prompt}]
        else:
            messages = conversation_history + [
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{user_input}"}
            ]
        # Print messages in blue color
        print(f"\033[94mmessages: {messages}\033[0m")
        response = send_message_to_model_with_history(messages)
        print(f"Model: {response}")
        # Add user and assistant turns to history
        conversation_history.append(messages[-1])
        conversation_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()