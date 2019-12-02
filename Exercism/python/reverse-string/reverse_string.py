def reverse(text):
    return "".join([text[-i] for i in range(1, len(text)+1)])
