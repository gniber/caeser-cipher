def encrypt(plaintext, shift):
	ciphertext = ""
	for c in plaintext.upper():
		if c.isalpha():
			ciphertext += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
		else:
			ciphertext += c
	return (ciphertext)

def decrypt(ciphertext, shift):
	plaintext = ""
	for c in ciphertext:
		if c.isalpha():
			plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
		else:
			plaintext += c
	return plaintext
