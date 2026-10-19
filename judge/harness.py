"""함수형(프로그래머스식) 문제 실행기: python harness.py <코드> <케이스.json>"""
import json
import sys


def to_jsonable(v):
    if isinstance(v, (list, tuple)):
        return [to_jsonable(x) for x in v]
    if isinstance(v, dict):
        return {str(k): to_jsonable(x) for k, x in v.items()}
    return v


def main():
    code_path, case_path = sys.argv[1], sys.argv[2]
    with open(case_path, encoding="utf-8") as f:
        case = json.load(f)
    with open(code_path, encoding="utf-8") as f:
        src = f.read()
    from runner import new_module
    ns = new_module("__solution__")
    exec(compile(src, "solution.py", "exec"), ns)
    fn = ns.get(case["func"])
    if fn is None:
        raise SystemExit(f"{case['func']} 함수가 정의되어 있지 않습니다.")
    result = fn(*case["args"])
    sys.stdout.write("\n" + json.dumps({"result": to_jsonable(result)}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    from runner import main as run_threaded  # 큰 스택 스레드에서 실행
    run_threaded(main)
