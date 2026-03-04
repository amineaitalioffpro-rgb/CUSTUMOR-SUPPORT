# Chargement du dataset

from datasets import load_dataset

ds = load_dataset("MakTek/Customer_support_faqs_dataset")


# Affichage des données

from pprint import pprint

data = ds['train']
pprint(data[1])
print("\n\n")


# Chargement API Key

from dotenv import load_dotenv

load_dotenv()


# Préparation des documents   -(Splitting + Structuration)-

from langchain_core.documents import Document

docs = []
for item in data:
    doc = Document(
        page_content='question:' + item['question'] + ' answer:' + item['answer']
    )
    docs.append(doc)
    
print(docs[1])
print("\n\n")
    


# Embeddings & LLM

from langchain_openai import OpenAIEmbeddings, ChatOpenAI

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model_name="gpt-3.5-turbo")


# Test du LLM

question = "how can i pay"
result = llm.invoke(question)
print(result.content)


# Création et stockage FAISS

from langchain_community.vectorstores import FAISS
import os

VECTOR_DB_PATH = "vector_db"

if os.path.exists(VECTOR_DB_PATH):
    vectordb = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local(VECTOR_DB_PATH)


# Création du Retriever

retriever = vectordb.as_retriever(search_kwargs={"k": 2})    


# Test du Retriever

results = retriever.invoke("how can i pay")
print(results)
print("\n\n\n\n")



# -------------------------------------------------------
# Création de la chaîne conversationnelle

from langchain.chains import ConversationalRetrievalChain

chat_bot = ConversationalRetrievalChain.from_llm(llm, retriever)


# Boucle interactive du chatbot

chat_history = []
while True:
    question = input("You: ")
    if question.lower() in ['quit', 'q', 'bye']:
        print("Bot: bye")
        break

    result = chat_bot.invoke({
        'question': question,
        'chat_history': chat_history
    })

    print("Bot:", result["answer"])
    chat_history.append((question, result['answer']))
