from agents import (
    research_agent,
    simplify_agent,
    summarize_agent,
    format_agent,
    mcq_agent
)

def academic_workflow(topic):
    research = research_agent(topic)
    simplified = simplify_agent(research)
    summary = summarize_agent(simplified)
    formatted_notes = format_agent(summary)
    mcqs = mcq_agent(summary)

    return {
        "topic": topic,
        "simplified": simplified,
        "summary": summary,
        "formatted_notes": formatted_notes,
        "mcqs": mcqs
    }
