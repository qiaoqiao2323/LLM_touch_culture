import openai
import os
import time



# Set your OpenAI API key here
openai.api_key = key


def generate_tactile_behaviors(emotion, encoder="Humanoid Robot", decoder="Human", culture="Belgian"):
    prompt = f"""Imagine you are an {encoder} tasked with communicating the {emotion} solely through touch to {decoder} in a {culture} cultural context. 
    You are to make contact with a human's bare arm—from the elbow to the end of the hand—using any form of touch you deem appropriate.
     Think carefully about how you want to express {emotion} in this cultural setting, and consider both static touches (like squeezing or patting) and dynamic actions (such as pushing, lifting, or shaking).

Please provide 10 distinct tactile behaviors that you would use to express {emotion}. For each behavior, include:
1. A brief description of the touch behavior (for example, forcefully pushing away, a vigorous grab followed by a sudden release, etc.).
2. A description of how the intensity of the touch communicates the emotion (using adjectives like 'firm', 'forceful', 'explosive', etc.).
3. A description of the rhythm or timing of the behavior (for example, a rapid, repetitive motion or a sudden, impactful gesture).
4. Take into account the cultural context into the tactile behaviors you choose.

Avoid using numeric scales or specific numerical values; instead, use descriptive language to convey the intensity and timing. Your response should be solely based on tactile communication and take into account the cultural context."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "You are a creative assistant skilled in generating tactile communication strategies."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']


def main():
    # List of emotions to generate tactile behaviors for
    emotions = [
        "fear"
    ]
    decoder = "Human"  # Can be changed to "robot" if desired
    culture = "Chinese"  # Modify culture as desired (e.g., "Spanish", "Japanese", etc.)
    encoder = "Humanoid Robot"  # Can be changed to "Human" if desired
    # "anger", "disgust", "fear", "happiness", "sadness",
    # "surprise", "sympathy", "embarrassment", "love",
    # "envy", "pride", "gratitude"

    # Create an output directory to store the files
    output_dir = "tactile_behaviors_human_Belgian"
    os.makedirs(output_dir, exist_ok=True)

    for emotion in emotions:
        print(f"Generating tactile behaviors for '{emotion}' (encoder: {encoder}, decoder: {decoder}, culture: {culture})...")
        try:
            result = generate_tactile_behaviors(emotion, encoder, decoder, culture)
        except Exception as e:
            print(f"Error generating for {emotion}: {e}")
            result = f"Error generating tactile behaviors for {emotion}: {e}"
        # Define file name and write the result to a text file
        file_name = f"{emotion}_{encoder}_{decoder}_{culture}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Saved tactile behaviors for '{emotion}' to {file_path}")
        # Optional: sleep to avoid rate limits
        time.sleep(3)


if __name__ == "__main__":
    main()
