from walletClient import WalletClient


wallet = WalletClient()

# print Addresses
addresses = wallet.show_address()
print(addresses)
