from walletClient import WalletClient

wallet = WalletClient()
# print wallets balance
bal = wallet.get_balance()
print(bal)
