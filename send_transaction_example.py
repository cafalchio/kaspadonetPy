from walletClient import WalletClient

wallet = WalletClient()
address = ""
password =''
print(wallet.send(to_address=address, amount=1, password=password))
