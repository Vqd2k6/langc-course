# from importlib.metadata import version
# from dotenv import load_dotenv
# load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI

# core_version = version("langchain-core")
# lg_version = version("langgraph")

# print(f"LangChain-Core Version: {core_version}")
# print(f"LangChain-Graph Version: {lg_version}")


# def main():
#     fast_llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
#     response = fast_llm.invoke("Say 'setup is completed successfully' in one word only")
    
#     text_content = response.content[0]["text"] if isinstance(response.content, list) else response.content
#     print(f"Response from Gemini: {text_content}")


# if __name__ == "__main__":
#     main()


from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser  # 👈 Import OutputParser

def main():
    # Model 1: Gemini 3.6 Flash
    llm_flash = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
    chain_flash = llm_flash | StrOutputParser()
    response_flash = chain_flash.invoke("Say 'setup is completed successfully' in one word only")
    
    # Model 2: Gemini 3.5 Flash
    llm_flash2 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    chain_flash2 = llm_flash2 | StrOutputParser()
    response_flash2 = chain_flash2.invoke("Say 'setup is completed successfully' in one word only")

    print(f"Response (Flash 3.6): {response_flash}")
    print(f"Response (Flash 3.5): {response_flash2}")




if __name__ == "__main__":
    main()

    