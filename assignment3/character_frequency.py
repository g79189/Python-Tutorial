def character_frequency(text):
    frequency={}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(character_frequency("hello world"))
