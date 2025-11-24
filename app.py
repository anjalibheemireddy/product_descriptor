import streamlit as st
import requests
import io

# --- Streamlit page config ---
st.set_page_config(page_title="Product JSON Bot", layout="wide")
st.title("🛍️ Product JSON Extractor ")

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display previous messages ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User input ---
if prompt := st.chat_input("Paste a product description here 👇"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Call FastAPI backend ---
    with st.chat_message("assistant"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/extract-json",
                json={"description": prompt},
                timeout=30  # optional: prevent hanging
            ).json()
            output_json = response.get("output_json", "{}")
        except Exception as e:
            output_json = f'{{"error": "Failed to get response from API: {e}"}}'

        st.markdown(f"```json\n{output_json}\n```")

    # --- Save conversation in session ---
    st.session_state.messages.append({"role": "assistant", "content": output_json})

# --- Export Chat as text file ---
st.markdown("---")
st.subheader("💾 Export Chat")
if st.button("Download Chat"):
    if st.session_state.messages:
        chat_text = "\n\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.messages])
        buffer = io.BytesIO(chat_text.encode("utf-8"))
        st.download_button("📥 Save Chat", buffer, file_name="ProductJSONBot_Chat.txt")
    else:
        st.warning("No chat history yet!")
