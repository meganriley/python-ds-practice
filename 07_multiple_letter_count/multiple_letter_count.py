def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    frequency_dict = {}
    for letter in phrase:
        if letter not in frequency_dict:
            frequency_dict.add(letter, 1)
        else:
            frequency_dict[letter] =+ 1

    return frequency_dict