import pytest


def count_words(filename):
    """Reads a text file and counts the frequency of each word.

    Args:
        filename (str): The name of the file to read.

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count


def test_count_words():
    # Create a temporary file for testing
    content = "apple banana apple cherry banana"
    with open('test_file.txt', 'w') as file:
        file.write(content)

    # Test word count
    assert count_words('test_file.txt') == {'apple': 2, 'banana': 2, 'cherry': 1}

    # Clean up the temporary file
    import os
    os.remove('test_file.txt')


if __name__ == '__main__':
    pytest.main(['-v'])
