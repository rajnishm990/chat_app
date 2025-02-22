
## AI-Powered PDF Q&A Chat App

This application allows users to upload PDFs, extract text, store embeddings, and ask questions about the content.  It uses LangChain for PDF processing and embedding generation, PgVector for efficient vector storage in PostgreSQL, and Streamlit for the user interface.

## Tools and Frameworks

*   **Python:** Programming language
*   **LangChain:** Framework for building LLM applications
*   **HuggingFace all-MiniLM-L6-v2:**  Embedding model
*   **PostgreSQL:** Database for storing embeddings
*   **PgVector:** PostgreSQL extension for vector search
*   **Streamlit:** Framework for building interactive web apps
*   **PyPDF** PDF processing library

## Setup and Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rajnishm990/chat_app.git
    cd chat_app
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up PostgreSQL:**
    *   Install PostgreSQL.
    *   Create a database and user (replace placeholders in `backend.py`).
    *   Enable the `pgvector` extension in your database:
        ```sql
        CREATE EXTENSION vector;
        ```


5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

6.  **Access the application:** Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

# Key Architectural Decisions and Trade-offs

## 1 Supabase for Database and Vector Storage
**Decision:** Used **Supabase Postgres** with **pgvector** for storing document embeddings.

**Reasoning:**  
- **Managed solution:** Avoids the need to set up and maintain a separate Postgres database.  
- **Built-in pgvector support:** Eliminates the need for third-party vector databases like Pinecone.  
- **Security & ease of use:** Supabase provides built-in authentication and access control.

**Trade-off:**  
- **Limited control over infrastructure** → If scaling is needed, a dedicated vector database like Weaviate  might be better.  
- **IPv4 restrictions in Supabase** → Faced connectivity issues initially since Supabase defaults to IPv6.  

---

## 2️ Streamlit for Frontend and Deployment
**Decision:** Used **Streamlit** for both the frontend and backend, skipping a separate API layer.  

**Reasoning:**  
- **Faster iteration:** This was an assignment, so the priority was a working prototype over full backend complexity.  
- **Minimal setup:** Streamlit allows handling UI and logic in a single codebase without API calls.  
- **Simplifies deployment:** Avoids the hassle of deploying both a backend (FastAPI/Django) and a frontend separately.  

**Trade-off:**  
- **Limited control over API endpoints & request handling.**  
- **Not ideal for production:** If this project grows, I would refactor it into a **backend-first** structure with FastAPI/Django exposing APIs and a separate frontend.  

**Alternative Considered:**  
- **Backend-first approach:** Normally, I'd build a **Django/FastAPI backend** with a separate UI, but Streamlit reduced complexity for a rapid AI prototype.  

---

## 3️ Hugging Face `sentence-transformers` for Embeddings
**Decision:** Used `sentence-transformers` from Hugging Face to generate document embeddings.

**Reasoning:**  
- **Pre-trained models available:** Avoids the need for training a custom embedding model.  
- **Efficient vector generation:** Works well with **pgvector** in Supabase.  

**Trade-off:**  
- **Fixed model:** If a more domain-specific model is needed, fine-tuning would be required.  
- **Latency considerations:** Local model inference is slightly slower than dedicated cloud-hosted embeddings (e.g., OpenAI API).  

---

## 4️ Deployment on Streamlit Cloud
**Decision:** Deployed directly on **Streamlit Community Cloud**.

**Reasoning:**  
- **One-click deployment:** Eliminates the need for setting up a separate backend infrastructure.  
- **Integrated UI hosting:** No need to configure a separate frontend deployment.  
- **Free-tier availability:** Perfect for a proof-of-concept project.  

**Trade-off:**  
- **Limited customization of deployment settings.**  
- **Performance constraints in free-tier hosting.**  

---

##  **Live Deployment**
🔗 **[LangPDFChat](https://langpdfchat.streamlit.app/)**  

## Conclusion
The architecture prioritizes **ease of development, quick deployment, and minimal infrastructure overhead** while ensuring a **functional AI-powered backend**. Future improvements could involve **switching to a dedicated vector database** and optimizing model serving for faster response times.  

---

 *Since my expertise lies in backend development, I focused on integrating AI efficiently rather than fine-tuning models. I'm eager to explore more ML techniques in future projects.*
