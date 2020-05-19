import krpc


if __name__ == "__main__":
    conn = krpc.connect(name="Example Connection",
                        address="192.168.1.151", rpc_port=50000, stream_port=50001)
    vessel = conn.space_center.active_vessel
    print(vessel)
