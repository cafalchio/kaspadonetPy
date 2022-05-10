import protos.kaspawalletd_pb2_grpc as gpb2
import protos.kaspawalletd_pb2 as pb2
import grpc


# Maybe open and close the channel on each use???? Need to ask someone.

class WalletClient:
    '''Creates a connection with the local wallet.
    '''
    def __init__(self, url = "localhost:8082"):
        self.url = url
    
    def get_balance(self):
        '''Returns the balance of a public address'''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            return stub.GetBalance(pb2.GetBalanceRequest())
    
    def create_unsigned_transaction(self, address, value):
        '''Create an unsigned Kaspa transaction'''
        message = pb2.CreateUnsignedTransactionsRequest(address=address, value=value)
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            return stub.CreateUnsignedTransactionsRequest(message)

    def show_address(self):
        '''Returns all generated public addresses of the current wallet'''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            return stub.ShowAddresses(pb2.ShowAddressesRequest())

    def new_address(self):
        '''Generates new public address of the current wallet and returns it'''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            return stub.NewAddress(pb2.NewAddressRequest())

    def broadcast(self, transactions):
        '''Broadcast the given transaction'''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            return stub.Broadcast(pb2.BroadcastRequest(transactions=transactions))

    def shutdown(self):
        '''Shutdown the wallet server'''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            return stub.Shutdown(pb2.ShutdownRequest())

    def send(self, to_address, amount, password):
        ''' '''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            amount*=100000000
            message = pb2.SendRequest(toAddress=to_address, amount=amount, password=password)
            return stub.Send(message)

    def sign(self, unsigned_transactions, password):
        '''Sign the given partially signed transaction'''
        with grpc.insecure_channel(self.url) as channel:
            stub = gpb2.kaspawalletdStub(self.channel)
            message = pb2.SignRequest(unsignedTransactions=unsigned_transactions, password=password)
            return stub.Sign(message)