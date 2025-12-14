from agents import create_agent

def main():
    # Create Gemini-based agent
    agent = create_agent()

    print("Milestone 2 Agent is ready.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ")

        if query.strip().lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Use .invoke with input dictionary
            response = agent.invoke({"input": query})
            print("Agent:", response["output"])

        except Exception as e:
            print("Error:", str(e))


if __name__ == "__main__":
    main()
