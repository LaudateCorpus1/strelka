# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from strelka.proto import mmbot_pb2 as strelka_dot_proto_dot_mmbot__pb2


class MmbotStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendVba = channel.unary_unary(
        '/Mmbot/SendVba',
        request_serializer=strelka_dot_proto_dot_mmbot__pb2.Vba.SerializeToString,
        response_deserializer=strelka_dot_proto_dot_mmbot__pb2.Prediction.FromString,
        )


class MmbotServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendVba(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MmbotServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendVba': grpc.unary_unary_rpc_method_handler(
          servicer.SendVba,
          request_deserializer=strelka_dot_proto_dot_mmbot__pb2.Vba.FromString,
          response_serializer=strelka_dot_proto_dot_mmbot__pb2.Prediction.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Mmbot', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))