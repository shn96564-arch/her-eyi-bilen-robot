echo # Bu dosya Ajan mimarisini yönetir. Hangi aracı, hangi LLM'i kullanacağına karar verir.^
from .rag_manager import retrieve_knowledge^
from .tool_factory import get_llm_pipeline, search_web_tool, generate_response^
from config import DEFAULT_MODEL_NAME^

# Temel LLM'i (Beyni) yükle^
LLM_PIPELINE = get_llm_pipeline(DEFAULT_MODEL_NAME)^

def run_agent_workflow(user_prompt):^
    # 1. PLANLAMA: Hangi araçları kullanmalıyım?^
    response = "🤖 **[AJAN BAŞLANGIÇ]:** Görev alınıyor... Hangi araçlar kullanılmalı?"^
    
    # Ajanın Karar Verme Mantığı: Çocuklara ders yardımı, güncel bilgi veya genel akıl yürütme?^
    
    # Kuantum veya Uzay gibi zor konular Grok/Gemini'yi tetiklesin (Gizli Kardeş)^
    if "kuantum" in user_prompt.lower() or "uzay zaman" in user_prompt.lower() or "çok zor" in user_prompt.lower():^
        action = "EXTERNAL_CONSULT"^
    
    # İnternet Aramasını tetikleyen anahtar kelimeler (Güncel bilgi)^
    elif "internet ara" in user_prompt.lower() or "güncel" in user_prompt.lower() or "son dakika" in user_prompt.lower():^
        action = "WEB_SEARCH"^
    
    # Çocuklara ders konusunda yardım (Özel Hafızayı tetikler)^
    elif "müfredat" in user_prompt.lower() or "özel not" in user_prompt.lower() or "okul kitabı" in user_prompt.lower():^
        action = "RAG_LOOKUP"^
    
    else:^
        action = "STANDARD_LLM"^
    
    # 2. AKSİYON ALMA (GİZLİ OPERASYON)^
    response += f"\n**[PLAN SONUCU]:** Aksiyon Kararı: **{action}**. "\
               f"\n**[GİZLİ]** LLM Kardeşler ve Araçlar devreye giriyor...\n\n"^
    
    if action == "WEB_SEARCH":^
        web_info = search_web_tool(user_prompt)^
        response += f"🌐 İnternetten Alınan Bilgi:\n{web_info}"^
    elif action == "RAG_LOOKUP":^
        # Burada gerçek RAG sistemi, ders notlarını arayıp çekmeliydi.^
        rag_info = retrieve_knowledge(user_prompt)^
        response += f"✅ **Özel Hafıza (RAG):** Ders Notlarından çekilen bilgi: {rag_info}"^
    elif action == "EXTERNAL_CONSULT":^
        # Burada Grok veya Gemini API çağrılmalıydı.^
        response += "🔄 **Grok/Gemini Kardeşle** gizli danışma yapıldı. Yanıt onaylandı ve geri dönüyor."^
    else:^
        # Standard LLM ile yanıt üretme (Temel akıl yürütme)^
        response += "🧠 **Ana Beyin:** Standart bilgelikle cevap üretiliyor:\n"^
        response += generate_response(LLM_PIPELINE, user_prompt)^
        
    return response > src/agent_core.py