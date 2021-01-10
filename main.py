alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alpha.upper()

def cipher(text, key):
	enc_txt = ""
	for char in text:
		if char.isupper() == True:
			raw_pos = ALPHA.find(char)
			enc_txt += ALPHA[(raw_pos + abs(key)) % 26]
		elif char.islower() == True:
			raw_pos = alpha.find(char)
			enc_txt += alpha[(raw_pos + abs(key)) % 26]
		elif char == " ":
			enc_txt += " "
		else:
			enc_txt += char
	return enc_txt

def decipher(text, key):
	dec_txt = ""
	for char in text:
		if char.isupper() == True:
			raw_pos = ALPHA.find(char)
			dec_txt += ALPHA[(raw_pos + key) % 26]
		elif char.islower() == True:
			raw_pos = alpha.find(char)
			dec_txt += alpha[(raw_pos + key) % 26]
		elif char == " ":
			dec_txt += " "
		else:
			dec_txt += char
	return dec_txt

def main():
	text = input("Enter Text: ")
	key = int(input("Enter Key: "))
	print("Encrypted: ", cipher(text, key), " | Decrypted: ", decipher(cipher(text, key), (abs(key)) * -1), "\n")

if __name__ == "__main__":
	main()
