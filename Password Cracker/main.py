import hashlib

def crackHash(inputPass):
    try:
        passFile = open("rockyou-35.txt", "r")

    except:
        print("Could not find file.")

    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()


        if digest == inputPass:
            print("Password Found: " + password)

if __name__ == '__main__':
    crackHash("da866cabf093419a02d56b080e03072f")
