def make_sentence(word,parts_of_speech):
    if parts_of_speech== 0:
        print(f"I am excited to add this{word}to my vast collection of them!")
    elif parts_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
        
    elif parts_of_speech== 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")
        
word = input("enter a verb,noun or adjective:")
parts_of_speech = int(input("type 0 for noun,1 for verb and 2 for adjective:"))
make_sentence(word,parts_of_speech)
        


