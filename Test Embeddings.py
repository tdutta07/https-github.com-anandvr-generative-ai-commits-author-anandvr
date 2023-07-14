import openai, numpy as np

resp = openai.Embedding.create(
    input=["samplemetadata", "Media_Ontology"],
    engine="text-embedding-ada-002")

embedding_a = resp['data'][0]['embedding']
embedding_b = resp['data'][1]['embedding']

similarity_score = np.dot(embedding_a, embedding_b)
print(embedding_a)
print (similarity_score)
