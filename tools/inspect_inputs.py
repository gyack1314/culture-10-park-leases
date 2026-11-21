"""核对本地资料文件的完整性与字段结构。"""
from pathlib import Path
import hashlib
import json

def inspect(root):
    root = Path(root)
    catalog = json.loads((root / "data/catalog.json").read_text(encoding="utf-8"))
    result = {}
    for name, entry in catalog["tables"].items():
        data = (root / "data" / (name + ".jsonl")).read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError("资料校验和不匹配：" + name)
        records = [json.loads(line) for line in data.decode("utf-8").splitlines() if line]
        if len(records) != entry["count"]:
            raise ValueError("资料行数不匹配：" + name)
        keys = set(entry["fields"])
        for record in records:
            if set(record) != keys:
                raise ValueError("资料字段不匹配：" + name)
        result[name] = len(records)
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="核对资料完整性")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(inspect(args.root), ensure_ascii=False, sort_keys=True))
