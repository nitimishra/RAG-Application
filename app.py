import streamlit as st
import importlib.util

# Load 4_history_aware_generation.py
spec = importlib.util.spec_from_file_location(
    "history_module",
    "4_history_aware_generation.py"
)

history_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(history_module)

st.set_page_config(page_title="RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("📄 RAG Chatbot")
st.write("Ask questions about your uploaded documents.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip():

        st.session_state.messages.append(
    {"role": "user", "content": question}
)

        try:
            with st.spinner("Generating answer..."):

                docs, answer = history_module.ask_question(question)

            st.subheader("🔍 Retrieved Documents")

            for i, doc in enumerate(docs, 1):
                with st.expander(f"Document {i}"):
                    st.write(doc.page_content)

            st.subheader("🤖 Final Answer")
            st.success(answer)

            st.session_state.messages.append(
    {"role": "assistant", "content": answer}
)

        except Exception:
            st.error("⚠️ AI service is temporarily unavailable. Please try again in a few minutes.")