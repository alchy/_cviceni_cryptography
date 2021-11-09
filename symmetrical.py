import base64

key = 'abcd0000000000000000000000000000'

key_b64 = base64.b64encode(key.encode("utf-8"))

data = 'message...'

data_encoded = fernet.encrypt(data.encode())

print('[d] encoded: ' + str(data_encoded))

data_decoded = fernet.decrypt(data_encoded).decode()

print('[d] decoded: ' + data_decoded)
