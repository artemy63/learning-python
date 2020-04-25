# https://py.checkio.org/mission/secret-message/


def find_message(text):
    """Find 111a secret message"""
    # arr = []
    # for letter in text:
    #     if letter.isupper():
    #         arr.append(letter)
    # return "".join(arr)

    # or
    return ''.join([i for i in text if i.isupper()])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")