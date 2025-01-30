def letter_probability(word, target_letter=None, letter_type=None):
    """
    Calculates the probability of selecting a specific type of letter 
    from a given word.

    :param word: The word to choose a letter from.
    :param target_letter: (Optional) The specific letter whose probability is calculated.
    :param letter_type: (Optional) Specify "vowel" or "consonant" for probability.
    :return: Probability of selecting the specified letter or type.
    """
    word = word.lower()
    total_letters = len(word)
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = sum(1 for letter in word if letter in vowels)
    consonant_count = total_letters - vowel_count
    
    if letter_type == "vowel":
        return vowel_count / total_letters
    elif letter_type == "consonant":
        return consonant_count / total_letters
    elif target_letter:
        target_count = word.count(target_letter.lower())
        return target_count / total_letters
    else:
        return "Invalid input"

# Example Usage
word = "association"
prob_vowel = letter_probability(word, letter_type="vowel")
prob_consonant = letter_probability(word, letter_type="consonant")
prob_s = letter_probability(word, target_letter="s")

print(f"Probability of choosing a vowel: {prob_vowel:.4f}")
print(f"Probability of choosing a consonant: {prob_consonant:.4f}")
print(f"Probability of choosing 'S': {prob_s:.4f}")
