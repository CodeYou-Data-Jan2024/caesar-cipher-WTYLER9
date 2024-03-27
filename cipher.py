sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
shift = 5
encrypted = []
li = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

for i in sentence:
    if i in li:
        index = (li.index(i) + shift)%26
        encrypted.append(li[index])
    else:
        encrypted.append(i)

print("The encrypted sentence is:", "".join(encrypted))