from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Streamlit Cloud: reads from st.secrets
# Local: reads from secret_key.py
# Hugging Face: reads from environment variables
try:
    import streamlit as st
    groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    try:
        from secret_key import groq_api_key
    except ImportError:
        groq_api_key = os.environ.get("GROQ_API_KEY", "")

os.environ["GROQ_API_KEY"] = groq_api_key

llm = ChatGroq(temperature=0.7, model_name="llama-3.3-70b-versatile")
parser = StrOutputParser()


def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Return only the name, nothing else."
    )

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated string."
    )

    name_chain = prompt_template_name | llm | parser
    food_items_chain = prompt_template_items | llm | parser

    restaurant_name = name_chain.invoke({"cuisine": cuisine})
    menu_items = food_items_chain.invoke({"restaurant_name": restaurant_name})

    return {"restaurant_name": restaurant_name, "menu_items": menu_items}


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Nigerian"))
