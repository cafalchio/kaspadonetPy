import protos.kaspawalletd_pb2_grpc as gpb2
import protos.kaspawalletd_pb2 as pb2
import grpc


class WalletClient:
    '''Creates a connection with the local wallet.
    '''
    def __init__(self, url = "localhost:8082"):
        self.channel = grpc.insecure_channel(url)
        self.stub = gpb2.kaspawalletdStub(self.channel)
    
    def get_balance(self):
        '''Returns the balance of a public address'''
        return self.stub.GetBalance(pb2.GetBalanceRequest())
    
    def create_unsigned_transaction(self, address, value):
        '''Create an unsigned Kaspa transaction'''
        message = pb2.CreateUnsignedTransactionsRequest(address=address, value=value)
        self.stub.CreateUnsignedTransactionsRequest(message)

    def show_address(self):
        '''Returns all generated public addresses of the current wallet'''
        return self.stub.ShowAddresses(pb2.ShowAddressesRequest())

    def new_address(self):
        '''Generates new public address of the current wallet and returns it'''
        return self.stub.NewAddress(pb2.NewAddressRequest())

    def broadcast(self, transactions):
        '''Broadcast the given transaction'''
        return self.stub.Broadcast(pb2.BroadcastRequest(transactions=transactions))

    def shutdown(self):
        '''Shutdown the wallet server'''
        return self.stub.Shutdown(pb2.ShutdownRequest())

    def send(self, to_address, amount, password):
        ''' '''
        amount*=100000000
        message = pb2.SendRequest(toAddress=to_address, amount=amount, password=password)
        return self.stub.Send(message)

    def sign(self, unsigned_transactions, password):
        '''Sign the given partially signed transaction'''
        message = pb2.SignRequest(unsignedTransactions=unsigned_transactions, password=password)
        return self.stub.Sign(message)
