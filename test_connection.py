import krpc


if __name__ == "__main__":
    conn = krpc.connect()
    vessel = conn.space_center.active_vessel
    print(vessel)
