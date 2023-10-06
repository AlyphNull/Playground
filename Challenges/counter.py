def count_characters(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    special_characters = "!@#$%^&*()-_+=<>?/[]{}|\\,.:;\"'"
    
    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = sum(1 for char in input_string if char in consonants)
    special_character_count = sum(1 for char in input_string if char in special_characters)
    total_count = len(input_string)


    return vowel_count, consonant_count, special_character_count, total_count

# Example usage
input_string = input("Enter a string: ")
vowels, consonants, special_characters, total_count = count_characters(input_string)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of special characters:", special_characters)
print("Number of special characters:", total_count)
