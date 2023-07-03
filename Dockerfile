FROM dockergpt-base

# Copy local source documents
COPY /source_documents/* /source_documents/
ENV SOURCE_DIRECTORY="/source_documents"

# Copy source code
WORKDIR /app
COPY /src/* .

# Set model parameters
# Play with it to get the best performance for your hardware
ENV MODEL_N_CTX=5000
ENV TARGET_SOURCE_CHUNKS=4
ENV TOKENIZERS_PARALLELISM=false
CMD [ "python", "server.py" ]