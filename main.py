alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alpha.upper()
key = -13

def cipher(text):
	key = 13
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

def decipher(text):
	key = -13
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

while True:
	raw_txt = input("Enter text: ")
	print("Encrypted: ", cipher(raw_txt), " | Decrypted: ", decipher(cipher(raw_txt)), "\n")
