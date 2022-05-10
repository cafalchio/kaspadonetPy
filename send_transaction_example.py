from walletClient import WalletClient

wallet = WalletClient()
# send transaction
address = "your address"
password = 'your pass'
print(wallet.send(to_address=address, amount=1, password=password))
