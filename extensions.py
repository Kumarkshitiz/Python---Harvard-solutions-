#get user input
file = input("File Name: ")
#remove spaces and make it lower
file_name = file.lower().strip()
#if gif,jpg,jpeg png print image/extension
extension = [".gif","jpg","jpeg","png"]
if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name:
    print("image/jpeg")
elif ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".zip"  in file_name:
    print("application/zip")
elif ".txt" in file_name:
    print("text/plain")
#else print  "application/octet-stream"
else:
    print("application/octet-stream")
