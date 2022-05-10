from typing_extensions import Self
import grpc
import protos.messages_pb2 as pb2
import protos.messages_pb2_grpc as gpb2
import protos.rpc_pb2 as rpc_pb2
import protos.rpc_pb2_grpc as rpc_gpb2

# using Grpc.Core;
# using Kaspadontnet.Clients;
# using Protowire;

# namespace Kaspadotnet.Examples;

# public partial class RpcExamples
# {
#     public async Task GetUTXOsByAddressExample()
#     {
#         // Using port 16610 for devnet. Use 16210 for testnet, or don't pass a url for mainnet
#         using var kaspadClient = new KaspadClient("http://localhost:16210");
#         using var messageStream = kaspadClient.Client.MessageStream();
#         var getUTXOsRequest = new KaspadMessage
#         {
#             GetUtxosByAddressesRequest = new GetUtxosByAddressesRequestMessage
#             {
#                 Addresses = {"kaspa:qztqt2uhp38nankeehl796c8a2707f4zfvyyl9r4xyuk4vf3a5rg76qz8944m"} // change this to your address
#             }
#         };
#         await messageStream.RequestStream.WriteAsync(getUTXOsRequest);
#         await messageStream.ResponseStream.MoveNext();
#         var response = messageStream.ResponseStream.Current;
#         Console.WriteLine("UTXOs by address: (Printing only 1 for clarity)");
#         Console.WriteLine(response.GetUtxosByAddressesResponse.Entries.FirstOrDefault());
#     }
# }

channel = GrpcChannel.ForAddress(url);
kaspadClient = new RPC.RPCClient(channel);




def test():
    with grpc.insecure_channel("localhost:16110") as channel:
        stub = gpb2.RPC(channel)
        
        getUTXOsRequest = pb2.KaspadMessage()
        rpc_pb2.GetUtxosByAddressesRequestMessage(addresses = {"kaspa:qztqt2uhp38nankeehl796c8a2707f4zfvyyl9r4xyuk4vf3a5rg76qz8944m"})
        stub.MessageStream.


test()


