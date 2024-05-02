from googletrans import Translator, LANGUAGES

def get_supported_languages():
    return LANGUAGES

def translate_text(text, target_language='en'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        return f"Translation failed. Error: {str(e)}"

def main():
    print("Supported Languages:")
    for code, language in get_supported_languages().items():
        print(f"{code}: {language}")

    user_input = input("Enter a sentence: ")

    # Allow the user to choose the target language
    target_language = input("Enter the language code for the target language (e.g., 'fr' for French): ")

    # Validate target language
    if target_language not in get_supported_languages():
        print("Invalid target language code. Using English as default.")
        target_language = 'en'

    translated_text = translate_text(user_input, target_language)

    # Display the results
    print("\nTranslation Details:")
    print("Input Text: ", user_input)
    print("Target Language: ", get_supported_languages()[target_language])
    print("Translated Text: ", translated_text)

if __name__ == "__main__":
    main()
