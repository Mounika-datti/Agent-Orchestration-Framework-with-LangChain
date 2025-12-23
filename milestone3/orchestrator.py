from agents.research_agent import create_research_agent
from agents.summarization_agent import create_summarization_agent
from shared_memory import create_shared_memory

def run_pipeline(user_query):
    research_chain, research_memory = create_research_agent()
    summary_chain, summary_memory = create_summarization_agent()
    shared_memory = create_shared_memory()

    # Step 1: Research Agent
    research_result = research_chain.invoke(
        {"topic": user_query}
    ).content

    # Store in shared memory (Week 6)
    shared_memory.save_context(
        {"input": user_query},
        {"output": research_result}
    )

    # Step 2: Summarization Agent
    summary_result = summary_chain.invoke(
        {"research": research_result}
    ).content

    return research_result, summary_result
