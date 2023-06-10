import os

from chromadb.config import Settings


class Config:
    def __init__(self):
        self.db_directory = os.environ.get('DB_DIRECTORY', '/db')
        self.source_directory = os.environ.get(
            'SOURCE_DIRECTORY', '/source_documents')
        self.model_type = os.environ.get('MODEL_TYPE', 'GPT4All')
        self.model_path = os.environ.get(
            'MODEL_PATH', 'models/ggml-gpt4all-j-v1.3-groovy.bin')
        self.embeddings_model_name = os.environ.get(
            'EMBEDDINGS_MODEL_NAME', 'all-MiniLM-L6-v2')
        self.model_n_ctx = int(os.environ.get('MODEL_N_CTX', 1000))
        self.taget_source_chunks = int(
            os.environ.get('TARGET_SOURCE_CHUNKS', 4))
        self.chunk_size = int(os.environ.get('CHUNK_SIZE', 500))
        self.chunk_overlap = int(os.environ.get('CHUNK_OVERLAP', 50))

        self.chrome_settings = Settings(
            chroma_db_impl='duckdb+parquet',
            persist_directory=self.db_directory,
            anonymized_telemetry=False
        )
