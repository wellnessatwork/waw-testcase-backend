"""
Minimal gRPC server stub.
Run via: `python -m waw_identity.identity_srv`
Candidate will fill in DB + encryption.
"""

import concurrent.futures       # <‑‑ add
import grpc
from waw.identity.v0 import identity_pb2_grpc  # generated stubs

class IdentityServicer(identity_pb2_grpc.IdentityServiceServicer):
    # TODO: CRUD backed by encrypted SQLite
    pass

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=4))
    identity_pb2_grpc.add_IdentityServiceServicer_to_server(
        IdentityServicer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    print("[identity] gRPC server listening on 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
