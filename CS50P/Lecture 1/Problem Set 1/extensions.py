def main():
    file_name = input("File name:").lower().strip()
    print(media_type(file_name))

def media_type(file):
    if "." in file:
        type = file.rsplit(".",1)
    else:
        return "application/octet-stream"

    match type[1]:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()
