def encrypt(plaintext, shift):
	ciphertext = ""
	for c in plaintext.lower():
		if c.isalpha():
			ciphertext += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
		else:
			ciphertext += c
	return (ciphertext)

def decrypt(ciphertext, shift):
	plaintext = ""
	for c in ciphertext:
		if c.isalpha():
			plaintext += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
		else:
			plaintext += c
	return plaintext
