from .models import Document

def build_index():

    index = {}

    documents = Document.objects.all()

    for doc in documents:

        words = doc.content.lower().split()

        for word in words:

            if word not in index:
                index[word] = []

            if doc.id not in index[word]:
                index[word].append(doc.id)

    return index