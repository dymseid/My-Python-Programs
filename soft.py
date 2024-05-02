from transformers import pipeline

# Initialize the translation pipeline
translator = pipeline("translation_en_to_fr")

# Function to translate a string
def translate_text(text):
    return translator(text)['translation_text']

# Get the text to translate from the user
while True:
    english_text = input("Enter the text you want to translate (or enter 'q' to quit): ")
    if english_text.lower() == 'q':
        break
    if english_text:
        # Use the pipeline to translate the text
        french_text = translate_text(english_text)
        print(french_text)
    else:
        print("Please enter a non-empty string.")