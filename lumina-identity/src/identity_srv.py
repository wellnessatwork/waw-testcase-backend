"""
Minimal gRPC server stub.
Run via: `python -m lumina_identity.identity_srv`
Candidate will fill in DB + encryption.
"""
import grpc
from lumina.identity.v0 import identity_pb2_grpc  # generated after make build

class IdentityServicer(identity_pb2_grpc.IdentityServiceServicer):
    # TODO: implement CRUD backed by encrypted SQLite
    pass

def serve():
    server = grpc.server(thread_pool=grpc.futures.ThreadPoolExecutor(max_workers=4))
    identity_pb2_grpc.add_IdentityServiceServicer_to_server(IdentityServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
