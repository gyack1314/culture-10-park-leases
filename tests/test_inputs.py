"""现有检查只覆盖资料本身，不判断后续业务结果。"""
from pathlib import Path
import json
from tools.inspect_inputs import inspect
ROOT = Path(__file__).resolve().parents[1]

def test_catalog_files_and_fields():
    counts = inspect(ROOT)
    assert counts and all(n > 0 for n in counts.values())

def test_primary_keys():
    catalog = json.loads((ROOT / "data/catalog.json").read_text(encoding="utf-8"))
    for name, entry in catalog["tables"].items():
        rows = [json.loads(s) for s in (ROOT / "data" / (name+".jsonl")).read_text(encoding="utf-8").splitlines()]
        key = entry["primary_key"]
        values = [json.dumps([r[k] for k in key],sort_keys=True) for r in rows]
        assert len(values) == len(set(values)), name

def test_catalog_has_only_local_materials():
    catalog = json.loads((ROOT / "data/catalog.json").read_text(encoding="utf-8"))
    assert catalog["synthetic"] is True
    assert all('/' not in name and '..' not in name for name in catalog["tables"])
