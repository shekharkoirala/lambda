# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import recommendation_pb2 as proto_dot_recommendation__pb2


class RecommendationStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Recommend = channel.unary_unary(
        '/news_recommendation.Recommendation/Recommend',
        request_serializer=proto_dot_recommendation__pb2.RecommendationRequest.SerializeToString,
        response_deserializer=proto_dot_recommendation__pb2.RecommendationReply.FromString,
        )
    self.Update = channel.unary_unary(
        '/news_recommendation.Recommendation/Update',
        request_serializer=proto_dot_recommendation__pb2.UpdateRequest.SerializeToString,
        response_deserializer=proto_dot_recommendation__pb2.UpdateReply.FromString,
        )
    self.Similar = channel.unary_unary(
        '/news_recommendation.Recommendation/Similar',
        request_serializer=proto_dot_recommendation__pb2.SimilarRequest.SerializeToString,
        response_deserializer=proto_dot_recommendation__pb2.SimilarReply.FromString,
        )
    self.Status = channel.unary_unary(
        '/news_recommendation.Recommendation/Status',
        request_serializer=proto_dot_recommendation__pb2.StatusRequest.SerializeToString,
        response_deserializer=proto_dot_recommendation__pb2.StatusReply.FromString,
        )


class RecommendationServicer(object):
  """The greeting service definition.
  """

  def Recommend(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Similar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RecommendationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Recommend': grpc.unary_unary_rpc_method_handler(
          servicer.Recommend,
          request_deserializer=proto_dot_recommendation__pb2.RecommendationRequest.FromString,
          response_serializer=proto_dot_recommendation__pb2.RecommendationReply.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=proto_dot_recommendation__pb2.UpdateRequest.FromString,
          response_serializer=proto_dot_recommendation__pb2.UpdateReply.SerializeToString,
      ),
      'Similar': grpc.unary_unary_rpc_method_handler(
          servicer.Similar,
          request_deserializer=proto_dot_recommendation__pb2.SimilarRequest.FromString,
          response_serializer=proto_dot_recommendation__pb2.SimilarReply.SerializeToString,
      ),
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=proto_dot_recommendation__pb2.StatusRequest.FromString,
          response_serializer=proto_dot_recommendation__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'news_recommendation.Recommendation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
