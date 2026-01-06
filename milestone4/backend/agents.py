from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm import llm


def research_agent(topic):
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Provide detailed academic content on {topic}."
    )
    return LLMChain(llm=llm, prompt=prompt).run(topic)


def simplify_agent(content):
    prompt = PromptTemplate(
        input_variables=["content"],
        template="Explain the following in very simple language:\n{content}"
    )
    return LLMChain(llm=llm, prompt=prompt).run(content)


def summarize_agent(content):
    prompt = PromptTemplate(
        input_variables=["content"],
        template="Create short exam-oriented notes:\n{content}"
    )
    return LLMChain(llm=llm, prompt=prompt).run(content)


def format_agent(content):
    prompt = PromptTemplate(
        input_variables=["content"],
        template="""
Format with headings and bullet points for exam preparation.

Content:
{content}
"""
    )
    return LLMChain(llm=llm, prompt=prompt).run(content)


def mcq_agent(content):
    prompt = PromptTemplate(
        input_variables=["content"],
        template="""
Create 5 MCQs with 4 options each and show the correct answer.

Content:
{content}
"""
    )
    return LLMChain(llm=llm, prompt=prompt).run(content)
