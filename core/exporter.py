import json

def export(reviews, path):
    with open(path, "w") as f:
        json.dump([r.dict() for r in reviews], f, indent=2, default=str)
