def simple_chatbot(user_query):
    """
    A simple chatbot that responds to predefined financial queries with canned responses.
    """
    response = ""
    user_query = user_query.lower()

    if "total revenue" in user_query:
        response = "The average total revenue across the companies and fiscal years analyzed is approximately $212,357.78 million."
    elif "net income changed" in user_query or "net income growth" in user_query:
        response = "In the last year analyzed, net income growth showed variability: Microsoft had a slight increase, whereas Apple and Tesla saw decreases."
    elif "total assets" in user_query:
        response = "The average total assets across the companies for the analyzed period are about $265,080.67 million."
    elif "cash flow from operating activities" in user_query:
        response = "Cash flow from operating activities varied, with an average across companies and fiscal years at approximately $67,444 million."
    else:
        response = "Sorry, I can only provide information on predefined queries. Please ask about total revenue, net income changes, total assets, or cash flow from operating activities."

    return response


# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("Ask a financial query (type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            print("Exiting chatbot. Goodbye!")
            break
        print(simple_chatbot(user_input))
