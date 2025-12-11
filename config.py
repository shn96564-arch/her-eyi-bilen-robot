import os
# LLM AyarlarçDEFAULT_MODEL_NAME = 'distilgpt2'MAX_RESPONSE_LENGTH = 300
# RAG AyarlarçVECTOR_DB_PATH = os.path.join("data", "vector_db")DOCS_PATH = os.path.join("data", "docs")
# Gizli Kardeüler API Ayarlarç (Ortam deßiükenlerinden okunacak)# Bu anahtarlarç gÅvenlik iáin komut satçrçnda belirlemelisiniz.API_KEY_GOOGLE_SEARCH = os.environ.get("GOOGLE_SEARCH_API_KEY", "FAKE_KEY")GOOGLE_CSE_ID = os.environ.get("GOOGLE_CSE_ID", "FAKE_ID")API_KEY_EXTERNAL_LLM = os.environ.get("EXTERNAL_LLM_API_KEY", "FAKE_EXTERNAL_KEY") 
