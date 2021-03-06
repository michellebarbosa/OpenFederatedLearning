# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import openfl.proto.collaborator_aggregator_interface_pb2 as collaborator__aggregator__interface__pb2


class AggregatorStub(object):
    """we start with everything as "required" while developing / debugging. This forces correctness better.
    FIXME: move to "optional" once development is complete

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestJob = channel.unary_unary(
                '/openfl_proto.Aggregator/RequestJob',
                request_serializer=collaborator__aggregator__interface__pb2.JobRequest.SerializeToString,
                response_deserializer=collaborator__aggregator__interface__pb2.JobReply.FromString,
                )
        self.DownloadModel = channel.unary_stream(
                '/openfl_proto.Aggregator/DownloadModel',
                request_serializer=collaborator__aggregator__interface__pb2.ModelDownloadRequest.SerializeToString,
                response_deserializer=collaborator__aggregator__interface__pb2.DataStream.FromString,
                )
        self.UploadLocalModelUpdate = channel.stream_unary(
                '/openfl_proto.Aggregator/UploadLocalModelUpdate',
                request_serializer=collaborator__aggregator__interface__pb2.DataStream.SerializeToString,
                response_deserializer=collaborator__aggregator__interface__pb2.LocalModelUpdateAck.FromString,
                )
        self.UploadLocalMetricsUpdate = channel.unary_unary(
                '/openfl_proto.Aggregator/UploadLocalMetricsUpdate',
                request_serializer=collaborator__aggregator__interface__pb2.LocalValidationResults.SerializeToString,
                response_deserializer=collaborator__aggregator__interface__pb2.LocalValidationResultsAck.FromString,
                )


class AggregatorServicer(object):
    """we start with everything as "required" while developing / debugging. This forces correctness better.
    FIXME: move to "optional" once development is complete

    """

    def RequestJob(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadModel(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadLocalModelUpdate(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadLocalMetricsUpdate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AggregatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestJob': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestJob,
                    request_deserializer=collaborator__aggregator__interface__pb2.JobRequest.FromString,
                    response_serializer=collaborator__aggregator__interface__pb2.JobReply.SerializeToString,
            ),
            'DownloadModel': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadModel,
                    request_deserializer=collaborator__aggregator__interface__pb2.ModelDownloadRequest.FromString,
                    response_serializer=collaborator__aggregator__interface__pb2.DataStream.SerializeToString,
            ),
            'UploadLocalModelUpdate': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadLocalModelUpdate,
                    request_deserializer=collaborator__aggregator__interface__pb2.DataStream.FromString,
                    response_serializer=collaborator__aggregator__interface__pb2.LocalModelUpdateAck.SerializeToString,
            ),
            'UploadLocalMetricsUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadLocalMetricsUpdate,
                    request_deserializer=collaborator__aggregator__interface__pb2.LocalValidationResults.FromString,
                    response_serializer=collaborator__aggregator__interface__pb2.LocalValidationResultsAck.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'openfl_proto.Aggregator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Aggregator(object):
    """we start with everything as "required" while developing / debugging. This forces correctness better.
    FIXME: move to "optional" once development is complete

    """

    @staticmethod
    def RequestJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/openfl_proto.Aggregator/RequestJob',
            collaborator__aggregator__interface__pb2.JobRequest.SerializeToString,
            collaborator__aggregator__interface__pb2.JobReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/openfl_proto.Aggregator/DownloadModel',
            collaborator__aggregator__interface__pb2.ModelDownloadRequest.SerializeToString,
            collaborator__aggregator__interface__pb2.DataStream.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadLocalModelUpdate(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/openfl_proto.Aggregator/UploadLocalModelUpdate',
            collaborator__aggregator__interface__pb2.DataStream.SerializeToString,
            collaborator__aggregator__interface__pb2.LocalModelUpdateAck.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadLocalMetricsUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/openfl_proto.Aggregator/UploadLocalMetricsUpdate',
            collaborator__aggregator__interface__pb2.LocalValidationResults.SerializeToString,
            collaborator__aggregator__interface__pb2.LocalValidationResultsAck.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
