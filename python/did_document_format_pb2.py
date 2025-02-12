# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: did_document_format.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64id_document_format.proto\x12\x08\x64ocument\"z\n\x12VerificationMethod\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.document.VerificationType\x12\x12\n\ncontroller\x18\x03 \x01(\t\x12\x1a\n\x12publicKeyMultibase\x18\x04 \x01(\t\"S\n\tSignature\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.document.VerificationType\x12\x0e\n\x06issuer\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\t\"M\n\x08Metadata\x12\x10\n\x08plugType\x18\x01 \x01(\t\x12\r\n\x05power\x18\x02 \x01(\t\x12 \n\x06status\x18\x03 \x01(\x0e\x32\x10.document.Status\"\x8b\x01\n\x07Service\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.document.ServiceType\x12\x14\n\nstringData\x18\x03 \x01(\tH\x00\x12&\n\x08metadata\x18\x04 \x01(\x0b\x32\x12.document.MetadataH\x00\x42\x11\n\x0fserviceEndpoint\"\xcb\x01\n\x08\x44ocument\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncontroller\x18\x02 \x01(\t\x12\x39\n\x13verificationMethods\x18\x03 \x03(\x0b\x32\x1c.document.VerificationMethod\x12&\n\tsignature\x18\x04 \x01(\x0b\x32\x13.document.Signature\x12#\n\x08services\x18\x05 \x03(\x0b\x32\x11.document.Service\x12\x17\n\x0f\x61uthentications\x18\x06 \x03(\t*1\n\x0bServiceType\x12\x07\n\x03p2p\x10\x00\x12\x0b\n\x07payment\x10\x01\x12\x0c\n\x08metadata\x10\x02*(\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\x0f\n\x0bUNAVAILABLE\x10\x01*R\n\x10VerificationType\x12\x1e\n\x1a\x45\x64\x32\x35\x35\x31\x39VerificationKey2020\x10\x00\x12\x1e\n\x1aSr25519VerificationKey2020\x10\x01\x42YZWgithub.com/peaqnetwork/peaq-network-ev-charging-message-format/golang/document;documentb\x06proto3')

_SERVICETYPE = DESCRIPTOR.enum_types_by_name['ServiceType']
ServiceType = enum_type_wrapper.EnumTypeWrapper(_SERVICETYPE)
_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_VERIFICATIONTYPE = DESCRIPTOR.enum_types_by_name['VerificationType']
VerificationType = enum_type_wrapper.EnumTypeWrapper(_VERIFICATIONTYPE)
p2p = 0
payment = 1
metadata = 2
AVAILABLE = 0
UNAVAILABLE = 1
Ed25519VerificationKey2020 = 0
Sr25519VerificationKey2020 = 1


_VERIFICATIONMETHOD = DESCRIPTOR.message_types_by_name['VerificationMethod']
_SIGNATURE = DESCRIPTOR.message_types_by_name['Signature']
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
VerificationMethod = _reflection.GeneratedProtocolMessageType('VerificationMethod', (_message.Message,), {
  'DESCRIPTOR' : _VERIFICATIONMETHOD,
  '__module__' : 'did_document_format_pb2'
  # @@protoc_insertion_point(class_scope:document.VerificationMethod)
  })
_sym_db.RegisterMessage(VerificationMethod)

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATURE,
  '__module__' : 'did_document_format_pb2'
  # @@protoc_insertion_point(class_scope:document.Signature)
  })
_sym_db.RegisterMessage(Signature)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'did_document_format_pb2'
  # @@protoc_insertion_point(class_scope:document.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'did_document_format_pb2'
  # @@protoc_insertion_point(class_scope:document.Service)
  })
_sym_db.RegisterMessage(Service)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'did_document_format_pb2'
  # @@protoc_insertion_point(class_scope:document.Document)
  })
_sym_db.RegisterMessage(Document)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZWgithub.com/peaqnetwork/peaq-network-ev-charging-message-format/golang/document;document'
  _SERVICETYPE._serialized_start=675
  _SERVICETYPE._serialized_end=724
  _STATUS._serialized_start=726
  _STATUS._serialized_end=766
  _VERIFICATIONTYPE._serialized_start=768
  _VERIFICATIONTYPE._serialized_end=850
  _VERIFICATIONMETHOD._serialized_start=39
  _VERIFICATIONMETHOD._serialized_end=161
  _SIGNATURE._serialized_start=163
  _SIGNATURE._serialized_end=246
  _METADATA._serialized_start=248
  _METADATA._serialized_end=325
  _SERVICE._serialized_start=328
  _SERVICE._serialized_end=467
  _DOCUMENT._serialized_start=470
  _DOCUMENT._serialized_end=673
# @@protoc_insertion_point(module_scope)
