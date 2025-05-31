def format_user_input(user_input):
    """Format the user input for sending to the model."""
    return user_input.strip()

def handle_model_response(response):
    """Extract and return the relevant information from the model's response."""
    if 'error' in response:
        return f"Error: {response['error']}"
    return response.get('message', 'No response from model.')

def manage_chat_session():
    """Initialize and manage the chat session."""
    session_data = {
        'history': [],
        'active': True
    }
    return session_data