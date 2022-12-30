import zipfile

count = 1

with open('wordlist.txt','rb') as text:    # Opening our wordlist in read byte mode
    for entry in text.readlines():
        password = entry.strip()    # Extracting the word from the line
        try:
            with zipfile.ZipFile('crackMe.zip','r') as zf: # Our password protected zip-file
                zf.extractall(pwd=password)
                print('[%s] [+] Password found! - %s' % (count,password.decode('utf8'))) # To decode the password in normal string
                break   # Breaking the loop when the password is found

        except:
            print('[%s] [-] Password failed! - %s' % (count,password.decode('utf8')))
            count += 1  # Password not found, moving on to next line
            pass
