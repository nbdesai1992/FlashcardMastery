# utils/openAI.py
import openai

# Your OpenAI API key, replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'

# Set up the OpenAI API client
openai.api_key = API_KEY

def generate_question(question_type, content, user):
    """
    Generate a simulated exam question using OpenAI API.

    Args:
        question_type (str): The type of the question ('MCQ', 'ESSAY', 'FIB').
        content (str): The content of the question.
        user (User): The user object for whom the question is generated.

    Returns:
        str: The generated question.
    """
    try:
        # Call the OpenAI API to generate the question
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=content,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.2
        )
        generated_question = response['choices'][0]['text']

        # Save the generated question in the database (you need to define a model for this)
        # For example:
        # GeneratedQuestion.objects.create(type=question_type, content=generated_question, study_session=None, user=user)

        return generated_question

    except Exception as e:
        print(f"Error generating question: {e}")
        return None
