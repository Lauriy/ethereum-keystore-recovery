with open('keystore.json') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'correcthorsebatterystaple')
    # tip: do not save the key or password anywhere, especially into a shared source file