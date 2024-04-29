def convert(text: str) -> str:
    leet_dict = {
        "a":"@",
        "A":"4",
        "B":"8",
        "b":"8",
        "E":"3",
        "e":"3",
        "I":"!",
        "i":"!",
        "L":"1",
        "l":"1",
        "O":"0",
        "o":"0",
        "S":"5",
        "s":"5"
    }

    leet_text = ""
    for char in text:
        if char in leet_dict:
            leet_text += leet_dict[char]
        else:
            leet_text += char
    print(leet_text)
convert("AbeEs")