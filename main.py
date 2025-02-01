import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['USER_AGENT'] = 'python_curiousamish/1.0'

# location of document to load
files = [
    "./diet_plan1.txt"
]
# Load documents from Local
docs = [TextLoader(file).load() for file in files]
docs_list = [item for sublist in docs for item in sublist]

# Use a text splitter with specified chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=10
)

# Split into chunks
doc_splits = text_splitter.split_documents(docs_list)

# Create embeddings and store them in a vector store
embedding1=OllamaEmbeddings(model="deepseek-r1:7b", base_url="http://localhost:11434/")
vectorstore = SKLearnVectorStore.from_documents(
    documents=doc_splits,
    embedding=embedding1
)

retriever = vectorstore.as_retriever(k=4)

# Define prompt for the LLM
prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks. Use the following documents to answer the question. think as concise as ppossible. Use three sentences maximum and keep the answer concise:
    Question: {question}
    Documents: {documents}
    Answer:
    """,
    input_variables=["question", "documents"],
)

# Initialize the LLM with Llama 3.1 model
llm = ChatOllama(
    model="deepseek-r1:7b",
    base_url="http://localhost:11434/",
    temperature=0,
)

# Create a chain combining the prompt template and LLM
rag_chain = prompt | llm | StrOutputParser()

question="can you suggest a new vegetarian dish for dinner basaed on diet plan?"

 # Retrieve relevant documents
documents = retriever.invoke(question)
      # Extract content from retrieved documents
doc_texts = "\\n".join([doc.page_content for doc in documents])
        # Get the answer from the language model
answer = rag_chain.invoke({"question": question, "documents": doc_texts})
        
print("Answer:", answer)
