
def main():

    press = input("File name: ")
    typeOfFile = identifyFile(press)
    matchFile(typeOfFile)


def identifyFile(p):

    dispose, sep, newp =  p.partition(".")

    return newp

def matchFile(p):

    match p:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("image/pdf")
        case _:
            print("application/octet-stream")
        

main()
