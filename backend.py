import os
from langchain.document_loaders import PyPDFLoader  
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import PGVector
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

CONNECTION_STRING = f"postgresql://postgres.uyhpttrmsqcihuxaebhf:{DB_PASSWORD}@aws-0-us-west-1.pooler.supabase.com:5432/postgres"

embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model) 
#embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY) 
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

def process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)  
    documents = loader.load()
    docs = text_splitter.split_documents(documents)
    return docs

def clean_text(text):
   
    return text.replace("\x00", "")

def store_embeddings(docs):
    try:
      #conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
      cleaned_docs = []
      for doc in docs:
        doc.page_content = clean_text(doc.page_content)  
        cleaned_docs.append(doc)
      db = PGVector.from_documents(
            docs,
            embeddings,
            connection_string=CONNECTION_STRING,
            #collection_name="pdf_embeddings",  
        )
      return "Embeddings stored successfully!"
    except Exception as e:
        return f"Error storing embeddings: {e}"


def search_embeddings(query):
    try:
        db = PGVector(
            connection_string=CONNECTION_STRING,
            embedding_function=embeddings,
            #collection_name="pdf_embeddings",
        )
        
        results = db.similarity_search(query, k=3)  
        return results
    except Exception as e:
        return f"Error searching embeddings: {e}"
