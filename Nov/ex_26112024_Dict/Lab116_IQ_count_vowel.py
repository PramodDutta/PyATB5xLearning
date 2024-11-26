input_string = "hello, world!"
# a,e, i,o,u.
# vowel =

vowels = "aeiou"

vowels_count = 0
consonant_count = 0
result = dict()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1

print(vowels_count)
