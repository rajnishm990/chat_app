import os
import streamlit as st
from backend import process_pdf, store_embeddings, search_embeddings
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


st.title("PDF Chat")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    pdf_path = "uploaded.pdf"  # Temporary file
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Process PDF"):
        with st.spinner("Processing PDF..."):
            docs = process_pdf(pdf_path)
            result = store_embeddings(docs)
            st.write(result)
        os.remove(pdf_path)  # Clean up the temporary file

    query = st.text_input("Ask a question about the PDF:")
    if st.button("Get Answer"):
        if query:
            with st.spinner("Searching for answer..."):
                results = search_embeddings(query)
                if isinstance(results, list):  # Success check
                    if results:
                        for doc in results:
                            st.write(doc.page_content)  # Display answer
                    else:
                        st.write("No relevant answers found.")
                else:
                    st.error(results)
        else:
            st.warning("Please enter a question.")