import json

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def calculate_stats(deliveries):
    speeds = [d["speed"] for d in deliveries]

    avg_speed = sum(speeds) / len(speeds)

    good_length = sum(1 for d in deliveries if d["length"] == "good length")
    outside_off = sum(1 for d in deliveries if "off" in d["line"])

    stats = {
        "average_speed": round(avg_speed,2),
        "good_length": good_length,
        "outside_off": outside_off,
        "total_balls": len(deliveries)
    }
    return stats