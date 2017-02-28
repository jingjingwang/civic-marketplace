import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.cloud.proto.pubsub.v1.pubsub_pb2 as google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2


class SubscriberStub(object):
  """The service that an application uses to manipulate subscriptions and to
  consume messages from a subscription via the `Pull` method.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateSubscription = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/CreateSubscription',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.FromString,
        )
    self.GetSubscription = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/GetSubscription',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.GetSubscriptionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.FromString,
        )
    self.UpdateSubscription = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/UpdateSubscription',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.UpdateSubscriptionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.FromString,
        )
    self.ListSubscriptions = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/ListSubscriptions',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSubscriptionsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSubscriptionsResponse.FromString,
        )
    self.DeleteSubscription = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/DeleteSubscription',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.DeleteSubscriptionRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ModifyAckDeadline = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/ModifyAckDeadline',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ModifyAckDeadlineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Acknowledge = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/Acknowledge',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.AcknowledgeRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Pull = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/Pull',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PullRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PullResponse.FromString,
        )
    self.StreamingPull = channel.stream_stream(
        '/google.pubsub.v1.Subscriber/StreamingPull',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.StreamingPullRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.StreamingPullResponse.FromString,
        )
    self.ModifyPushConfig = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/ModifyPushConfig',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ModifyPushConfigRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListSnapshots = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/ListSnapshots',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSnapshotsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSnapshotsResponse.FromString,
        )
    self.CreateSnapshot = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/CreateSnapshot',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.CreateSnapshotRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Snapshot.FromString,
        )
    self.DeleteSnapshot = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/DeleteSnapshot',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.DeleteSnapshotRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Seek = channel.unary_unary(
        '/google.pubsub.v1.Subscriber/Seek',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.SeekRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.SeekResponse.FromString,
        )


class SubscriberServicer(object):
  """The service that an application uses to manipulate subscriptions and to
  consume messages from a subscription via the `Pull` method.
  """

  def CreateSubscription(self, request, context):
    """Creates a subscription to a given topic.
    If the subscription already exists, returns `ALREADY_EXISTS`.
    If the corresponding topic doesn't exist, returns `NOT_FOUND`.

    If the name is not provided in the request, the server will assign a random
    name for this subscription on the same project as the topic, conforming
    to the
    [resource name format](https://cloud.google.com/pubsub/docs/overview#names).
    The generated name is populated in the returned Subscription object.
    Note that for REST API requests, you must specify a name in the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSubscription(self, request, context):
    """Gets the configuration details of a subscription.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSubscription(self, request, context):
    """Updates an existing subscription. Note that certain properties of a
    subscription, such as its topic, are not modifiable.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListSubscriptions(self, request, context):
    """Lists matching subscriptions.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSubscription(self, request, context):
    """Deletes an existing subscription. All messages retained in the subscription
    are immediately dropped. Calls to `Pull` after deletion will return
    `NOT_FOUND`. After a subscription is deleted, a new one may be created with
    the same name, but the new one has no association with the old
    subscription or its topic unless the same topic is specified.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyAckDeadline(self, request, context):
    """Modifies the ack deadline for a specific message. This method is useful
    to indicate that more time is needed to process a message by the
    subscriber, or to make the message available for redelivery if the
    processing was interrupted. Note that this does not modify the
    subscription-level `ackDeadlineSeconds` used for subsequent messages.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Acknowledge(self, request, context):
    """Acknowledges the messages associated with the `ack_ids` in the
    `AcknowledgeRequest`. The Pub/Sub system can remove the relevant messages
    from the subscription.

    Acknowledging a message whose ack deadline has expired may succeed,
    but such a message may be redelivered later. Acknowledging a message more
    than once will not result in an error.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Pull(self, request, context):
    """Pulls messages from the server. Returns an empty list if there are no
    messages available in the backlog. The server may return `UNAVAILABLE` if
    there are too many concurrent pull requests pending for the given
    subscription.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamingPull(self, request_iterator, context):
    """(EXPERIMENTAL) StreamingPull is an experimental feature. This RPC will
    respond with UNIMPLEMENTED errors unless you have been invited to test
    this feature. Contact cloud-pubsub@google.com with any questions.

    Establishes a stream with the server, which sends messages down to the
    client. The client streams acknowledgements and ack deadline modifications
    back to the server. The server will close the stream and return the status
    on any error. The server may close the stream with status `OK` to reassign
    server-side resources, in which case, the client should re-establish the
    stream. `UNAVAILABLE` may also be returned in the case of a transient error
    (e.g., a server restart). These should also be retried by the client. Flow
    control can be achieved by configuring the underlying RPC channel.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyPushConfig(self, request, context):
    """Modifies the `PushConfig` for a specified subscription.

    This may be used to change a push subscription to a pull one (signified by
    an empty `PushConfig`) or vice versa, or change the endpoint URL and other
    attributes of a push subscription. Messages will accumulate for delivery
    continuously through the call regardless of changes to the `PushConfig`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListSnapshots(self, request, context):
    """Lists the existing snapshots.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSnapshot(self, request, context):
    """Creates a snapshot from the requested subscription.
    If the snapshot already exists, returns `ALREADY_EXISTS`.
    If the requested subscription doesn't exist, returns `NOT_FOUND`.

    If the name is not provided in the request, the server will assign a random
    name for this snapshot on the same project as the subscription, conforming
    to the
    [resource name format](https://cloud.google.com/pubsub/docs/overview#names).
    The generated name is populated in the returned Snapshot object.
    Note that for REST API requests, you must specify a name in the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSnapshot(self, request, context):
    """Removes an existing snapshot. All messages retained in the snapshot
    are immediately dropped. After a snapshot is deleted, a new one may be
    created with the same name, but the new one has no association with the old
    snapshot or its subscription, unless the same subscription is specified.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Seek(self, request, context):
    """Seeks an existing subscription to a point in time or to a given snapshot,
    whichever is provided in the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SubscriberServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateSubscription': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSubscription,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.SerializeToString,
      ),
      'GetSubscription': grpc.unary_unary_rpc_method_handler(
          servicer.GetSubscription,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.GetSubscriptionRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.SerializeToString,
      ),
      'UpdateSubscription': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSubscription,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.UpdateSubscriptionRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Subscription.SerializeToString,
      ),
      'ListSubscriptions': grpc.unary_unary_rpc_method_handler(
          servicer.ListSubscriptions,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSubscriptionsRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSubscriptionsResponse.SerializeToString,
      ),
      'DeleteSubscription': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSubscription,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.DeleteSubscriptionRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ModifyAckDeadline': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyAckDeadline,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ModifyAckDeadlineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Acknowledge': grpc.unary_unary_rpc_method_handler(
          servicer.Acknowledge,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.AcknowledgeRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Pull': grpc.unary_unary_rpc_method_handler(
          servicer.Pull,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PullRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PullResponse.SerializeToString,
      ),
      'StreamingPull': grpc.stream_stream_rpc_method_handler(
          servicer.StreamingPull,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.StreamingPullRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.StreamingPullResponse.SerializeToString,
      ),
      'ModifyPushConfig': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyPushConfig,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ModifyPushConfigRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListSnapshots': grpc.unary_unary_rpc_method_handler(
          servicer.ListSnapshots,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSnapshotsRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListSnapshotsResponse.SerializeToString,
      ),
      'CreateSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSnapshot,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.CreateSnapshotRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Snapshot.SerializeToString,
      ),
      'DeleteSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSnapshot,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.DeleteSnapshotRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Seek': grpc.unary_unary_rpc_method_handler(
          servicer.Seek,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.SeekRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.SeekResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.pubsub.v1.Subscriber', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PublisherStub(object):
  """The service that an application uses to manipulate topics, and to send
  messages to a topic.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTopic = channel.unary_unary(
        '/google.pubsub.v1.Publisher/CreateTopic',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Topic.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Topic.FromString,
        )
    self.Publish = channel.unary_unary(
        '/google.pubsub.v1.Publisher/Publish',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PublishRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PublishResponse.FromString,
        )
    self.GetTopic = channel.unary_unary(
        '/google.pubsub.v1.Publisher/GetTopic',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.GetTopicRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Topic.FromString,
        )
    self.ListTopics = channel.unary_unary(
        '/google.pubsub.v1.Publisher/ListTopics',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicsResponse.FromString,
        )
    self.ListTopicSubscriptions = channel.unary_unary(
        '/google.pubsub.v1.Publisher/ListTopicSubscriptions',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicSubscriptionsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicSubscriptionsResponse.FromString,
        )
    self.DeleteTopic = channel.unary_unary(
        '/google.pubsub.v1.Publisher/DeleteTopic',
        request_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.DeleteTopicRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class PublisherServicer(object):
  """The service that an application uses to manipulate topics, and to send
  messages to a topic.
  """

  def CreateTopic(self, request, context):
    """Creates the given topic with the given name.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Publish(self, request, context):
    """Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic
    does not exist. The message payload must not be empty; it must contain
    either a non-empty data field, or at least one attribute.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTopic(self, request, context):
    """Gets the configuration of a topic.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTopics(self, request, context):
    """Lists matching topics.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTopicSubscriptions(self, request, context):
    """Lists the name of the subscriptions for this topic.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTopic(self, request, context):
    """Deletes the topic with the given name. Returns `NOT_FOUND` if the topic
    does not exist. After a topic is deleted, a new topic may be created with
    the same name; this is an entirely new topic with none of the old
    configuration or subscriptions. Existing subscriptions to this topic are
    not deleted, but their `topic` field is set to `_deleted-topic_`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublisherServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTopic': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTopic,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Topic.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Topic.SerializeToString,
      ),
      'Publish': grpc.unary_unary_rpc_method_handler(
          servicer.Publish,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PublishRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.PublishResponse.SerializeToString,
      ),
      'GetTopic': grpc.unary_unary_rpc_method_handler(
          servicer.GetTopic,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.GetTopicRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.Topic.SerializeToString,
      ),
      'ListTopics': grpc.unary_unary_rpc_method_handler(
          servicer.ListTopics,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicsRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicsResponse.SerializeToString,
      ),
      'ListTopicSubscriptions': grpc.unary_unary_rpc_method_handler(
          servicer.ListTopicSubscriptions,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicSubscriptionsRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.ListTopicSubscriptionsResponse.SerializeToString,
      ),
      'DeleteTopic': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTopic,
          request_deserializer=google_dot_cloud_dot_proto_dot_pubsub_dot_v1_dot_pubsub__pb2.DeleteTopicRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.pubsub.v1.Publisher', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
