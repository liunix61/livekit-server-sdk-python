# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_webhook.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import livekit_egress_pb2 as livekit__egress__pb2
from . import livekit_ingress_pb2 as livekit__ingress__pb2
from . import livekit_models_pb2 as livekit__models__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="livekit_webhook.proto",
    package="livekit",
    syntax="proto3",
    serialized_options=b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x15livekit_webhook.proto\x12\x07livekit\x1a\x14livekit_models.proto\x1a\x14livekit_egress.proto\x1a\x15livekit_ingress.proto"\x82\x02\n\x0cWebhookEvent\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x1b\n\x04room\x18\x02 \x01(\x0b\x32\r.livekit.Room\x12-\n\x0bparticipant\x18\x03 \x01(\x0b\x32\x18.livekit.ParticipantInfo\x12(\n\x0b\x65gress_info\x18\t \x01(\x0b\x32\x13.livekit.EgressInfo\x12*\n\x0cingress_info\x18\n \x01(\x0b\x32\x14.livekit.IngressInfo\x12!\n\x05track\x18\x08 \x01(\x0b\x32\x12.livekit.TrackInfo\x12\n\n\x02id\x18\x06 \x01(\t\x12\x12\n\ncreated_at\x18\x07 \x01(\x03\x42\x46Z#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3',
    dependencies=[
        livekit__models__pb2.DESCRIPTOR,
        livekit__egress__pb2.DESCRIPTOR,
        livekit__ingress__pb2.DESCRIPTOR,
    ],
)


_WEBHOOKEVENT = _descriptor.Descriptor(
    name="WebhookEvent",
    full_name="livekit.WebhookEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="event",
            full_name="livekit.WebhookEvent.event",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="room",
            full_name="livekit.WebhookEvent.room",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="participant",
            full_name="livekit.WebhookEvent.participant",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="egress_info",
            full_name="livekit.WebhookEvent.egress_info",
            index=3,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ingress_info",
            full_name="livekit.WebhookEvent.ingress_info",
            index=4,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="track",
            full_name="livekit.WebhookEvent.track",
            index=5,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="livekit.WebhookEvent.id",
            index=6,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created_at",
            full_name="livekit.WebhookEvent.created_at",
            index=7,
            number=7,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=102,
    serialized_end=360,
)

_WEBHOOKEVENT.fields_by_name["room"].message_type = livekit__models__pb2._ROOM
_WEBHOOKEVENT.fields_by_name[
    "participant"
].message_type = livekit__models__pb2._PARTICIPANTINFO
_WEBHOOKEVENT.fields_by_name[
    "egress_info"
].message_type = livekit__egress__pb2._EGRESSINFO
_WEBHOOKEVENT.fields_by_name[
    "ingress_info"
].message_type = livekit__ingress__pb2._INGRESSINFO
_WEBHOOKEVENT.fields_by_name["track"].message_type = livekit__models__pb2._TRACKINFO
DESCRIPTOR.message_types_by_name["WebhookEvent"] = _WEBHOOKEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebhookEvent = _reflection.GeneratedProtocolMessageType(
    "WebhookEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _WEBHOOKEVENT,
        "__module__": "livekit_webhook_pb2"
        # @@protoc_insertion_point(class_scope:livekit.WebhookEvent)
    },
)
_sym_db.RegisterMessage(WebhookEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
