plain 		= ['A','B','C','D','E','F','G','H']
encrypted 	= ['F','A','D','B','H','G','C','E']


character_by_user = input() # masukkan character yg nk encrypt/decrypt dekat sini

get_location_plain = plain.index(character_by_user)
get_location_encrypted = encrypted.index(character_by_user)

encrypted_character = encrypted[get_location_plain]
decrypted_character = plain[get_location_encrypted]

print(encrypted_character)