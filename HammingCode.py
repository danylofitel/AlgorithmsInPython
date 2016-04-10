# Hamming code receives 4 bits as input at a time
K = 4


# Read in K bits at a time and write out those plus parity bits
def encode_hamming(message):
    result = ""
    while len(message) >= K:
        segment = message[0:K]
        result = result + hamming(segment)
        message = message[K:]
    return result


# Return given 4 bits plus parity bits for bits (1, 2, 3), (2, 3, 4) and (1, 3, 4)
def hamming(block):
    digit1 = parity(block, [0, 1, 2])
    digit2 = parity(block, [1, 2, 3])
    digit3 = parity(block, [0, 2, 3])

    return block + digit1 + digit2 + digit3


# Compute the parity bit for the given message and indices
def parity(message, indices):
    sub = ""
    for index in indices:
        sub += message[index]
    return str(str.count(sub, "1") % 2)


input_string = raw_input()
formatted_input = ""
for c in input_string:
    if c == '0' or c == '1':
        formatted_input += c

formatted_input += "".join(['0' for i in range(abs(K - len(formatted_input) % K) % K)])

print "Input string : " + formatted_input
print "Output string: " + encode_hamming(formatted_input)
