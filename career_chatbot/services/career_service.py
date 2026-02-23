from core.chain import get_chain
from langchain_core.messages import HumanMessage, AIMessage
from utils.logger import logger

class CareerAdvisorService:

    def __init__(self):
        self.chain = get_chain()
        self.chat_history = []
        self.total_tokens = 0

    def get_response(self, user_input):
        try:
            # Convert stored tuples to LangChain message format
            formatted_history = []
            for role, message in self.chat_history:
                if role == "human":
                    formatted_history.append(HumanMessage(content=message))
                elif role == "ai":
                    formatted_history.append(AIMessage(content=message))

            # Invoke the chain
            response = self.chain.invoke({
                "input": user_input,
                "chat_history": formatted_history
            })

            
            logger.info(f"Successfully generated response for User Input: {user_input[:50]}...")

            # Save conversation
            self.chat_history.append(("human", user_input))
            self.chat_history.append(("ai", response))

            return response
            
        except Exception as e:
            logger.error(f"Error in CareerAdvisorService: {str(e)}")
            return "I apologize, but I'm having trouble connecting to my Gemini brain right now. Please try again in a moment."

    def get_token_stats(self):
        return self.total_tokens