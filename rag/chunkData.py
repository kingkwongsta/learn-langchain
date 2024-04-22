import pandas as pd
from datasets import load_dataset
from pinecone import Index

from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# Load the Hugging Face dataset
dataset = load_dataset("brianarbuckle/cocktail_recipes", split="train")

pc = Pinecone(api_key=PINECONE_API_KEY)
use_serverless = True
index_name = 'panda'
spec = ServerlessSpec(cloud='aws', region='us-west-2')
index = pc.Index(index_name)

model_name = 'text-embedding-ada-002'
embeddings = OpenAIEmbeddings(
    model=model_name,
    openai_api_KEY=OPENAI_API_KEY
)
text_field = "text"  # This will be used for embedding the recipe content
vectorstore = PineconeVectorStore(
    index, embeddings, text_field
)

# Chunk the dataset by row
chunk_size = 100
chunks = [dataset[i:i + chunk_size] for i in range(0, len(dataset), chunk_size)]

# Process each chunk
for chunk in chunks:
  # Convert the chunk to a pandas DataFrame
  df = pd.DataFrame(chunk)

  # Prepare data for Document objects
  documents = []
  for _, row in df.iterrows():  # Iterate over rows using iterrows
    # Extract relevant data from the row
    data = {
      'column_names': list(df.columns),  # Get column names
      'title': row['title'],  # Assuming a "title" column exists
      'ingredients': row['ingredients'],  # Assuming an "ingredients" column exists
      'directions': row['directions'],  # Assuming a "directions" column exists
      'misc': row.get('misc', None),  # Get "misc" if it exists, otherwise None
      'source': row['source'],  # Assuming a "source" column exists
      'ner': None  # Placeholder for NER information (implement later)
    }

    # Add the data to the documents list
    documents.append(Document(page_content=row['ingredients'] + " " + row['directions']))  # Combine ingredients and directions


  # Implement Named Entity Recognition (NER) - Replace with your chosen library
  # This is a placeholder; you'll need to install and use a specific NER library.
  # Here's an example using spaCy (assuming it's installed):
  # from spacy.en import English
  # nlp = English()
  # for doc in documents:
  #   text = doc.data['ingredients'] + " " + doc.data['directions']  # Combine text for NER
  #   doc_nlp = nlp(text)
  #   entities = [(ent.text, ent.label_) for ent in doc_nlp.ents]  # Extract entities and labels
  #   doc.data['ner'] = entities  # Add NER information to data

  # Add the chunk to the vector store
  vectorstore.add_documents(documents, batch_size=chunk_size)

# Close the Pinecone index
index.close()
