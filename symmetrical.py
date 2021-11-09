from cryptography.fernet import Fernet
import hashlib
import base64

APP_SC = '12341234123412341234123412341234'


def encrypt(data, sc):

    try:

        key = hashlib.md5(APP_SC.encode() + sc.encode()).hexdigest()

        fernet = Fernet(base64.b64encode(key.encode("utf-8")))

        return fernet.encrypt(data.encode()).decode()

    except Exception as e:

        return '[!] encrypt: ' + repr(e)


def decrypt(data, sc):

    try:

        key = hashlib.md5(APP_SC.encode() + sc.encode()).hexdigest()

        fernet = Fernet(base64.b64encode(key.encode("utf-8")))

        return fernet.decrypt(data.encode()).decode()

    except Exception as e:

        return '[!] decrypt: ' + repr(e)
