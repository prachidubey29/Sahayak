import chromadb
def create_vector_store(chunks):
    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="hcltech_report"
    )
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk["text"]],
            ids=[str(i)],
            metadatas=[{"page": chunk["page"]}]
        )
    return collection