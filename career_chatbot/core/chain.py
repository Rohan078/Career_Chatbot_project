from core.llm import get_llm
from core.prompts import get_career_prompt

from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

def get_chain():
    llm = get_llm()
    prompt = get_career_prompt()

    chain = prompt | llm | StrOutputParser()

    return chain