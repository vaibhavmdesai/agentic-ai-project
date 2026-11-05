from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra='ignore')
    aws_endpoint_url:str='http://localhost:9000'
    aws_region:str='us-east-1'
    aws_access_key_id:str=''
    aws_secret_access_key:str=''
    s3_bucket:str=''
    database_url:str=''  # Render PostgreSQL External Database URL
    openai_api_key:str=''
    openai_embed_model:str=''
    openai_chat_model:str=''
    max_upload_bytes:int=10485760
    pinecone_api_key:str=''
    pinecone_index_name:str='atlas-enterprise-ai-index'
    pinecone_cloud:str='aws'
    pinecone_region:str='us-east-1'
    pinecone_ready_timeout:int=180
    rius_api_key:str=''
    rius_service_name:str='atlas-ai-enterprise'
    rius_disabled:bool=False
    rius_capture_content:bool=False
    min_relevance:float=0.25
    hitl_enabled:bool=True
    memory_turns:int=6

@lru_cache
def settings() -> Settings:
    return Settings()