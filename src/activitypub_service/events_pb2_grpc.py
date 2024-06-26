# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import events_pb2 as events__pb2


class EventServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEvent = channel.unary_unary(
                '/events.EventService/GetEvent',
                request_serializer=events__pb2.GetEventRequest.SerializeToString,
                response_deserializer=events__pb2.GetEventResponse.FromString,
                )
        self.GetEventsChronologically = channel.unary_unary(
                '/events.EventService/GetEventsChronologically',
                request_serializer=events__pb2.GetEventsChronologicallyRequest.SerializeToString,
                response_deserializer=events__pb2.GetEventsChronologicallyResponse.FromString,
                )


class EventServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventsChronologically(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEvent,
                    request_deserializer=events__pb2.GetEventRequest.FromString,
                    response_serializer=events__pb2.GetEventResponse.SerializeToString,
            ),
            'GetEventsChronologically': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventsChronologically,
                    request_deserializer=events__pb2.GetEventsChronologicallyRequest.FromString,
                    response_serializer=events__pb2.GetEventsChronologicallyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'events.EventService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/GetEvent',
            events__pb2.GetEventRequest.SerializeToString,
            events__pb2.GetEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventsChronologically(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/events.EventService/GetEventsChronologically',
            events__pb2.GetEventsChronologicallyRequest.SerializeToString,
            events__pb2.GetEventsChronologicallyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
