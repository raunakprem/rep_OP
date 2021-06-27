import dropbox 
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token


    def upload_file (self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f= open (file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main ():
    access_token='sl.AzWs0oCx2lENhVL-MlNKtUzmx83ZNZWPgsmS1742D47d8ItmxMZ_NeA9Hzf-EyeYk6_0FNVtE8OLCJ7940FuSRnVjSekIjz7c41_ByMYZZ-BmCOnAqw27pU6BkeeLq_zbejmPGFf'
    transferData=TransferData(access_token)

    file_from=input("enter the file path to trasfer")
    file_to=input ("enter the full path to upload on dropbox")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()     
        