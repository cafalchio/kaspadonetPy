# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kaspawalletd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12kaspawalletd.proto\x12\x0ckaspawalletd\"\x13\n\x11GetBalanceRequest\"p\n\x12GetBalanceResponse\x12\x11\n\tavailable\x18\x01 \x01(\x04\x12\x0f\n\x07pending\x18\x02 \x01(\x04\x12\x36\n\x0f\x61\x64\x64ressBalances\x18\x03 \x03(\x0b\x32\x1d.kaspawalletd.AddressBalances\"F\n\x0f\x41\x64\x64ressBalances\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x11\n\tavailable\x18\x02 \x01(\x04\x12\x0f\n\x07pending\x18\x03 \x01(\x04\"D\n!CreateUnsignedTransactionsRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\"B\n\"CreateUnsignedTransactionsResponse\x12\x1c\n\x14unsignedTransactions\x18\x01 \x03(\x0c\"\x16\n\x14ShowAddressesRequest\"(\n\x15ShowAddressesResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x03(\t\"\x13\n\x11NewAddressRequest\"%\n\x12NewAddressResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"(\n\x10\x42roadcastRequest\x12\x14\n\x0ctransactions\x18\x01 \x03(\x0c\"\"\n\x11\x42roadcastResponse\x12\r\n\x05txIDs\x18\x01 \x03(\t\"\x11\n\x0fShutdownRequest\"\x12\n\x10ShutdownResponse\"B\n\x0bSendRequest\x12\x11\n\ttoAddress\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x10\n\x08password\x18\x03 \x01(\t\"&\n\x0cSendResponse\x12\x16\n\x0etransactionIDs\x18\x01 \x03(\t\"=\n\x0bSignRequest\x12\x1c\n\x14unsignedTransactions\x18\x01 \x03(\x0c\x12\x10\n\x08password\x18\x02 \x01(\t\"*\n\x0cSignResponse\x12\x1a\n\x12signedTransactions\x18\x01 \x03(\x0c\x32\xb3\x05\n\x0ckaspawalletd\x12Q\n\nGetBalance\x12\x1f.kaspawalletd.GetBalanceRequest\x1a .kaspawalletd.GetBalanceResponse\"\x00\x12\x81\x01\n\x1a\x43reateUnsignedTransactions\x12/.kaspawalletd.CreateUnsignedTransactionsRequest\x1a\x30.kaspawalletd.CreateUnsignedTransactionsResponse\"\x00\x12Z\n\rShowAddresses\x12\".kaspawalletd.ShowAddressesRequest\x1a#.kaspawalletd.ShowAddressesResponse\"\x00\x12Q\n\nNewAddress\x12\x1f.kaspawalletd.NewAddressRequest\x1a .kaspawalletd.NewAddressResponse\"\x00\x12K\n\x08Shutdown\x12\x1d.kaspawalletd.ShutdownRequest\x1a\x1e.kaspawalletd.ShutdownResponse\"\x00\x12N\n\tBroadcast\x12\x1e.kaspawalletd.BroadcastRequest\x1a\x1f.kaspawalletd.BroadcastResponse\"\x00\x12?\n\x04Send\x12\x19.kaspawalletd.SendRequest\x1a\x1a.kaspawalletd.SendResponse\"\x00\x12?\n\x04Sign\x12\x19.kaspawalletd.SignRequest\x1a\x1a.kaspawalletd.SignResponse\"\x00\x42\x36Z4github.com/kaspanet/kaspad/cmd/kaspawallet/daemon/pbb\x06proto3')



_GETBALANCEREQUEST = DESCRIPTOR.message_types_by_name['GetBalanceRequest']
_GETBALANCERESPONSE = DESCRIPTOR.message_types_by_name['GetBalanceResponse']
_ADDRESSBALANCES = DESCRIPTOR.message_types_by_name['AddressBalances']
_CREATEUNSIGNEDTRANSACTIONSREQUEST = DESCRIPTOR.message_types_by_name['CreateUnsignedTransactionsRequest']
_CREATEUNSIGNEDTRANSACTIONSRESPONSE = DESCRIPTOR.message_types_by_name['CreateUnsignedTransactionsResponse']
_SHOWADDRESSESREQUEST = DESCRIPTOR.message_types_by_name['ShowAddressesRequest']
_SHOWADDRESSESRESPONSE = DESCRIPTOR.message_types_by_name['ShowAddressesResponse']
_NEWADDRESSREQUEST = DESCRIPTOR.message_types_by_name['NewAddressRequest']
_NEWADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['NewAddressResponse']
_BROADCASTREQUEST = DESCRIPTOR.message_types_by_name['BroadcastRequest']
_BROADCASTRESPONSE = DESCRIPTOR.message_types_by_name['BroadcastResponse']
_SHUTDOWNREQUEST = DESCRIPTOR.message_types_by_name['ShutdownRequest']
_SHUTDOWNRESPONSE = DESCRIPTOR.message_types_by_name['ShutdownResponse']
_SENDREQUEST = DESCRIPTOR.message_types_by_name['SendRequest']
_SENDRESPONSE = DESCRIPTOR.message_types_by_name['SendResponse']
_SIGNREQUEST = DESCRIPTOR.message_types_by_name['SignRequest']
_SIGNRESPONSE = DESCRIPTOR.message_types_by_name['SignResponse']
GetBalanceRequest = _reflection.GeneratedProtocolMessageType('GetBalanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBALANCEREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.GetBalanceRequest)
  })
_sym_db.RegisterMessage(GetBalanceRequest)

GetBalanceResponse = _reflection.GeneratedProtocolMessageType('GetBalanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBALANCERESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.GetBalanceResponse)
  })
_sym_db.RegisterMessage(GetBalanceResponse)

AddressBalances = _reflection.GeneratedProtocolMessageType('AddressBalances', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBALANCES,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.AddressBalances)
  })
_sym_db.RegisterMessage(AddressBalances)

CreateUnsignedTransactionsRequest = _reflection.GeneratedProtocolMessageType('CreateUnsignedTransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUNSIGNEDTRANSACTIONSREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.CreateUnsignedTransactionsRequest)
  })
_sym_db.RegisterMessage(CreateUnsignedTransactionsRequest)

CreateUnsignedTransactionsResponse = _reflection.GeneratedProtocolMessageType('CreateUnsignedTransactionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUNSIGNEDTRANSACTIONSRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.CreateUnsignedTransactionsResponse)
  })
_sym_db.RegisterMessage(CreateUnsignedTransactionsResponse)

ShowAddressesRequest = _reflection.GeneratedProtocolMessageType('ShowAddressesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHOWADDRESSESREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.ShowAddressesRequest)
  })
_sym_db.RegisterMessage(ShowAddressesRequest)

ShowAddressesResponse = _reflection.GeneratedProtocolMessageType('ShowAddressesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHOWADDRESSESRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.ShowAddressesResponse)
  })
_sym_db.RegisterMessage(ShowAddressesResponse)

NewAddressRequest = _reflection.GeneratedProtocolMessageType('NewAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWADDRESSREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.NewAddressRequest)
  })
_sym_db.RegisterMessage(NewAddressRequest)

NewAddressResponse = _reflection.GeneratedProtocolMessageType('NewAddressResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWADDRESSRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.NewAddressResponse)
  })
_sym_db.RegisterMessage(NewAddressResponse)

BroadcastRequest = _reflection.GeneratedProtocolMessageType('BroadcastRequest', (_message.Message,), {
  'DESCRIPTOR' : _BROADCASTREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.BroadcastRequest)
  })
_sym_db.RegisterMessage(BroadcastRequest)

BroadcastResponse = _reflection.GeneratedProtocolMessageType('BroadcastResponse', (_message.Message,), {
  'DESCRIPTOR' : _BROADCASTRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.BroadcastResponse)
  })
_sym_db.RegisterMessage(BroadcastResponse)

ShutdownRequest = _reflection.GeneratedProtocolMessageType('ShutdownRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.ShutdownRequest)
  })
_sym_db.RegisterMessage(ShutdownRequest)

ShutdownResponse = _reflection.GeneratedProtocolMessageType('ShutdownResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.ShutdownResponse)
  })
_sym_db.RegisterMessage(ShutdownResponse)

SendRequest = _reflection.GeneratedProtocolMessageType('SendRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.SendRequest)
  })
_sym_db.RegisterMessage(SendRequest)

SendResponse = _reflection.GeneratedProtocolMessageType('SendResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.SendResponse)
  })
_sym_db.RegisterMessage(SendResponse)

SignRequest = _reflection.GeneratedProtocolMessageType('SignRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNREQUEST,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.SignRequest)
  })
_sym_db.RegisterMessage(SignRequest)

SignResponse = _reflection.GeneratedProtocolMessageType('SignResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNRESPONSE,
  '__module__' : 'kaspawalletd_pb2'
  # @@protoc_insertion_point(class_scope:kaspawalletd.SignResponse)
  })
_sym_db.RegisterMessage(SignResponse)

_KASPAWALLETD = DESCRIPTOR.services_by_name['kaspawalletd']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/kaspanet/kaspad/cmd/kaspawallet/daemon/pb'
  _GETBALANCEREQUEST._serialized_start=36
  _GETBALANCEREQUEST._serialized_end=55
  _GETBALANCERESPONSE._serialized_start=57
  _GETBALANCERESPONSE._serialized_end=169
  _ADDRESSBALANCES._serialized_start=171
  _ADDRESSBALANCES._serialized_end=241
  _CREATEUNSIGNEDTRANSACTIONSREQUEST._serialized_start=243
  _CREATEUNSIGNEDTRANSACTIONSREQUEST._serialized_end=311
  _CREATEUNSIGNEDTRANSACTIONSRESPONSE._serialized_start=313
  _CREATEUNSIGNEDTRANSACTIONSRESPONSE._serialized_end=379
  _SHOWADDRESSESREQUEST._serialized_start=381
  _SHOWADDRESSESREQUEST._serialized_end=403
  _SHOWADDRESSESRESPONSE._serialized_start=405
  _SHOWADDRESSESRESPONSE._serialized_end=445
  _NEWADDRESSREQUEST._serialized_start=447
  _NEWADDRESSREQUEST._serialized_end=466
  _NEWADDRESSRESPONSE._serialized_start=468
  _NEWADDRESSRESPONSE._serialized_end=505
  _BROADCASTREQUEST._serialized_start=507
  _BROADCASTREQUEST._serialized_end=547
  _BROADCASTRESPONSE._serialized_start=549
  _BROADCASTRESPONSE._serialized_end=583
  _SHUTDOWNREQUEST._serialized_start=585
  _SHUTDOWNREQUEST._serialized_end=602
  _SHUTDOWNRESPONSE._serialized_start=604
  _SHUTDOWNRESPONSE._serialized_end=622
  _SENDREQUEST._serialized_start=624
  _SENDREQUEST._serialized_end=690
  _SENDRESPONSE._serialized_start=692
  _SENDRESPONSE._serialized_end=730
  _SIGNREQUEST._serialized_start=732
  _SIGNREQUEST._serialized_end=793
  _SIGNRESPONSE._serialized_start=795
  _SIGNRESPONSE._serialized_end=837
  _KASPAWALLETD._serialized_start=840
  _KASPAWALLETD._serialized_end=1531
# @@protoc_insertion_point(module_scope)
