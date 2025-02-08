import streamlit as st
import main

def run_app():
    st.set_page_config(page_title="Chat with PDFs")
    st.title("Chat with PDFs with Deepseek")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type="pdf",
        accept_multiple_files=False
    )

    if uploaded_file:
        try:
            file_path = main.upload_pdf(uploaded_file)
            db = main.create_vector_store(file_path)
            question = st.chat_input()

            if question:
                st.chat_message("user").write(question)
                related_documents = main.retrieve_docs(db, question)
                answer = main.question_pdf(question, related_documents)
                st.chat_message("assistant").write(answer)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    run_app()