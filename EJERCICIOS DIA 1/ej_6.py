import random
import string

def generate_password(length):
    if length < 3:
        print("La longitud mínima de la contraseña debe ser al menos 3.")
        return None

    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    password = random.choice(letters) + random.choice(numbers) + random.choice(special_chars)

    password += ''.join(random.choice(letters + numbers + special_chars) for _ in range(length - 3))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    length = int(input("Ingrese la longitud deseada para la contraseña (mínimo 3): "))
    password = generate_password(length)
    if password:
        print("Contraseña generada:", password)

if __name__ == "__main__":
    main()
