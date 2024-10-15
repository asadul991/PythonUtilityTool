def count_letters(text):
    text = text.lower()
    letter_count = 0

    for char in text:

        if char.isalpha():
            letter_count += 1
    
    return letter_count