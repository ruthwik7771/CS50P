from os.path import splitext

#introducing type_exists new function
def type_exists(file):

    #splitting the string into name and type
    name, type = splitext(file)

    type = type.replace(type[0], "")

    #tightening the code
    match type:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print(f"text/{name}")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


#input file name and stripping along with lowering at the same time
file = input("File name: ").strip().lower()

#if "." exists in the file name
if "." in file:
    type_exists(file)

#if "." doesn't exist in the file name
else:
    print("application/octet-stream")
