# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: output_file.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import onnx_common_pb2 as onnx__common__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='output_file.proto',
  package='aihwx',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11output_file.proto\x12\x05\x61ihwx\x1a\x11onnx_common.proto\x1a\x0c\x63ommon.proto\"I\n\x10\x45pochInformation\x12\r\n\x05\x65poch\x18\x01 \x02(\x05\x12&\n\x07metrics\x18\x02 \x03(\x0b\x32\x15.aihwx.AttributeProto\"\xa3\x01\n\x0eTrainingOutput\x12\x1f\n\x07version\x18\x01 \x02(\x0b\x32\x0e.aihwx.Version\x12\x1f\n\x07network\x18\x02 \x02(\x0b\x32\x0e.aihwx.Network\x12\'\n\x06\x65pochs\x18\x03 \x03(\x0b\x32\x17.aihwx.EpochInformation\x12&\n\x07metrics\x18\x04 \x03(\x0b\x32\x15.aihwx.AttributeProto')
  ,
  dependencies=[onnx__common__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])




_EPOCHINFORMATION = _descriptor.Descriptor(
  name='EpochInformation',
  full_name='aihwx.EpochInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='epoch', full_name='aihwx.EpochInformation.epoch', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='aihwx.EpochInformation.metrics', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=134,
)


_TRAININGOUTPUT = _descriptor.Descriptor(
  name='TrainingOutput',
  full_name='aihwx.TrainingOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='aihwx.TrainingOutput.version', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network', full_name='aihwx.TrainingOutput.network', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epochs', full_name='aihwx.TrainingOutput.epochs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='aihwx.TrainingOutput.metrics', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=300,
)

_EPOCHINFORMATION.fields_by_name['metrics'].message_type = onnx__common__pb2._ATTRIBUTEPROTO
_TRAININGOUTPUT.fields_by_name['version'].message_type = common__pb2._VERSION
_TRAININGOUTPUT.fields_by_name['network'].message_type = common__pb2._NETWORK
_TRAININGOUTPUT.fields_by_name['epochs'].message_type = _EPOCHINFORMATION
_TRAININGOUTPUT.fields_by_name['metrics'].message_type = onnx__common__pb2._ATTRIBUTEPROTO
DESCRIPTOR.message_types_by_name['EpochInformation'] = _EPOCHINFORMATION
DESCRIPTOR.message_types_by_name['TrainingOutput'] = _TRAININGOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EpochInformation = _reflection.GeneratedProtocolMessageType('EpochInformation', (_message.Message,), dict(
  DESCRIPTOR = _EPOCHINFORMATION,
  __module__ = 'output_file_pb2'
  # @@protoc_insertion_point(class_scope:aihwx.EpochInformation)
  ))
_sym_db.RegisterMessage(EpochInformation)

TrainingOutput = _reflection.GeneratedProtocolMessageType('TrainingOutput', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGOUTPUT,
  __module__ = 'output_file_pb2'
  # @@protoc_insertion_point(class_scope:aihwx.TrainingOutput)
  ))
_sym_db.RegisterMessage(TrainingOutput)


# @@protoc_insertion_point(module_scope)
