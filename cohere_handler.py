import cohere

co = cohere.Client("Ktcs8hTzcykhR1e978yzrcNBj6j8u4s1hHhOViSn")  # Your Cohere API key

def generate_with_cohere(prompt):
    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        if response.generations and response.generations[0].text.strip():
            return response.generations[0].text.strip()
        else:
            return "I'm not sure how to respond. Please try again."

    except Exception as e:
        print("Cohere error:", e)
        return "An error occurred while generating the response."
