import zipfile

def extract_file(zfile, password):
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        return password
    except Exception as error:
        print(error)

def main():
    zfile = zipfile.ZipFile("data.zip")
    pass_file = open('dictionary.txt')

    for line in pass_file.readlines():
        password = line.strip("\n")
        guess = extract_file(zfile, password=password)
        if guess:
            print(f"Contraseña correcta encontrada: {guess}")
            break

    pass_file.close()

if __name__ == "__main__":
    main()
