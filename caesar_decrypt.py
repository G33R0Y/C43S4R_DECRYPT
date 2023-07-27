def print_ascii_art():
    ascii_art = """
 _____   ___  _____  _____    ___ ______  ______ _____ _____ ________   _______ _____ 
/  __ \ /   ||____ |/  ___|  /   || ___ \ |  _  \  ___/  __ \| ___ \ \ / / ___ \_   _|
| /  \// /| |    / /\ `--.  / /| || |_/ / | | | | |__ | /  \/| |_/ /\ V /| |_/ / | |  
| |   / /_| |    \ \ `--. \/ /_| ||    /  | | | |  __|| |    |    /  \ / |  __/  | |  
| \__/\___  |.___/ //\__/ /\___  || |\ \  | |/ /| |___| \__/\| |\ \  | | | |     | |  
 \____/   |_/\____/ \____/     |_/\_| \_| |___/ \____/ \____/\_| \_| \_/ \_|     \_/  
                                                                                      
                                                                                      
    """
    print(ascii_art)

def caesar_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print_ascii_art()
    encrypted_text = input("Enter the encrypted text: ")
    print(" ")
    for key in range(26):
        decrypted_text = caesar_decrypt(encrypted_text, key)
        print(f"Key: {key} | Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()

