def decode_ways(s, index=0, path="", results=None):
    if results is None:
        results = []
    
    if index == len(s):
        results.append(path)
        return results
    
    # Single digit decoding
    num1 = int(s[index])
    if 1 <= num1 <= 9:
        decode_ways(s, index + 1, path + chr(64 + num1), results)
    
    # Double digit decoding
    if index + 1 < len(s):
        num2 = int(s[index:index+2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, path + chr(64 + num2), results)
    
    return results

encoded_message = input("Enter the encoded message: ")
possible_decodings = decode_ways(encoded_message)
print("Possible decoded messages:")
for decoding in possible_decodings:
    print(decoding)
