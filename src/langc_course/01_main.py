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
from langchain_core.output_parsers import StrOutputParser 

def main():
    # Model 1: Gemini 3.6 Flash
    llm_01 = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
    llm_01 = llm_01 | StrOutputParser()
    response_01 = llm_01.invoke("Say 'setup is completed successfully' in one word only")
    
    # Model 2: Gemini 3.5 Flash
    llm_02 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    llm_02 = llm_02 | StrOutputParser()
    response_02 = llm_02.invoke("Say 'setup is completed successfully' in one word only")

    print(f"Response (01): {response_01}")
    print(f"Response (02): {response_02}")

    print("Setup completed successfully")


if __name__ == "__main__":
    main()

    