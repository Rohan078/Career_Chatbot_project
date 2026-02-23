from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_career_prompt():

    system_prompt = """
    You are an expert AI Career Advisor.

    - Provide structured career guidance.
    - Suggest skills, certifications, roadmaps.
    - Ask clarifying questions when needed.
    - Be realistic and industry-aligned.
    """

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])