
def chunk_text(text, size=500, overlap=100 ):
    sentences = text.split(". ")
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current)+len(sentence) < size:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "

    if current:
        chunks.append(current.strip())

    return chunks


