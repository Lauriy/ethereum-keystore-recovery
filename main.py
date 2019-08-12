from web3 import Web3

with open('keystore.json') as keyfile:
    w3 = Web3(Web3.IPCProvider())
    encrypted_key = keyfile.read()
    with open('passwords.txt') as passwords_file:
        passwords_to_try = ['', ' ']
        passwords_to_try += passwords_file.read().splitlines()
        for password in passwords_to_try:
            try:
                print('Trying: ' + str(password))
                private_key = w3.eth.account.decrypt(encrypted_key, password)
                print('Got it! ' + private_key)
                break
            except ValueError:
                print('No dice.')
                continue
