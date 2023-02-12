print("hello world")
word= input("podaj słowo: ")
def nothing_special(word):
    output_text=''
    for letter in word:
        if letter in ['a','e','i','o','y', 'u']:
            output_text=''.join([output_text, "*"])
        else:
            output_text = ''.join([output_text,letter])
    return output_text

print(nothing_special(word))