import mimetypes

def guessMimeType():
    file_name = input("File Name: ")
    guess = mimetypes.guess_type(file_name, strict=True)
    
    if any(guess):
        print(guess[0])
    else:
        print("application/octet-stream")
    
guessMimeType()




