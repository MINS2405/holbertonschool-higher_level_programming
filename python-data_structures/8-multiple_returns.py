#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first_char = multiple_returns(sentence)
    print("Length: {}, First character: {}".format(length, first_char))
