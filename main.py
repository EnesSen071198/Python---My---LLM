from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

model = ChatOpenAI(temperature=0.3)#0 a yaklaştıkça daha net kesin detaylı cevaplar verir 1 e yaklaştıkça saçmalayabilme ihtimali var

message = (SystemMessage(content="Translate the following from English to Turkish"),
           HumanMessage(content="Hello"))

if __name__ == "__main__":
    response=model.invoke(message)
    print(response)
