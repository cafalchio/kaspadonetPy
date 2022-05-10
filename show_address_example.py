from walletClient import WalletClient


wallet = WalletClient()

# print Addresses
addresses = wallet.show_address()
print(addresses)


#####
# send transaction
# address = "your address"
# password = 'your pass'
# print(wallet.send(to_address=address, amount=1000, password=password))
