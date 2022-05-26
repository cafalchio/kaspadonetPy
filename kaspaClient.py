from pyexpat.errors import messages
import protos.messages_pb2_grpc as gpb2
import protos.messages_pb2 as pb2
import protos.rpc_pb2 as rpc_pb2
import grpc




class KaspaClient:
    '''Creates a connection with the local node.
    '''
    def __init__(self, url = "localhost:16111"):
        self.channel = grpc.insecure_channel(url)
        self.rpc = gpb2.RPCStub(self.channel)
     
    def GetBlockDagInfo(self):
        message = rpc_pb2.GetBlockDagInfo()
        return self.rpc.MessageStream()



    
    

kaspa = KaspaClient()
kaspa.RPCerror()
print(kaspa.GetCurrentNetworkResponseMessage())