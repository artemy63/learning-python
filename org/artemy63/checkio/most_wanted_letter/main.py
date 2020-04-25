import string


def checkio(text):
    # dict = {}
    # max_inclusion = 0
    # for letter in text.lower():
    #     if letter.isalpha():
    #         if dict.__contains__(letter):
    #             dict[letter] = dict[letter] + 1
    #         else:
    #             dict[letter] = 1
    #
    #         max_inclusion = max(max_inclusion, dict[letter])
    #
    # orderer_letters = []
    # for letter, count in dict.items():
    #     if count == max_inclusion:
    #         orderer_letters.append(letter)
    #
    # orderer_letters.sort()
    #
    # print(orderer_letters[0])

    #other solution
    text = text.lower()
    print(text.count)
    print(max(string.ascii_lowercase, key=text.count))
    return max(string.ascii_lowercase, key=text.count)

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("Hello World!") == "l", "Hello test"
#     assert checkio("How do you do?") == "o", "O is most wanted"
#     assert checkio("One") == "e", "All letter only once."
#     assert checkio("Oops!") == "o", "Don't forget about lower case."
#     assert checkio("AAaooo!!!!") == "a", "Only letters."
#     assert checkio("abe") == "a", "The First."
#     print("Start the long test")
#     assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#     print("The local tests are done.")


checkio("Hello World!")
checkio("How do you do?")
checkio("One")
checkio("Oops!")
checkio("AAaooo!!!!")
checkio("abe")
checkio("a" * 9000 + "b" * 1000)