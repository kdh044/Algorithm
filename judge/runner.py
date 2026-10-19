"""표준입출력형 실행기: python runner.py <코드>
재귀 깊은 풀이가 가능하도록 큰 스택의 스레드에서 실행한다 (백준 PyPy와 비슷한 깊이).
"""
import os
import sys
import threading
import traceback
import types

STACK = 200 * 1024 * 1024


def new_module(name):
    """평범한 dict 대신 진짜 모듈 공간에서 실행 (PyPy는 dict로 exec하면 전역 변수 접근이 몇 배 느려짐)"""
    mod = types.ModuleType(name)
    mod.__file__ = "solution.py"
    sys.modules[name] = mod
    return mod.__dict__


def run(path, globs):
    src = open(path, encoding="utf-8").read()
    exec(compile(src, "solution.py", "exec"), globs)


def main(target):
    code = [0]

    def body():
        try:
            target()
        except SystemExit as e:
            c = e.code
            if c is None:
                code[0] = 0
            elif isinstance(c, int):
                code[0] = c
            else:
                sys.stderr.write(str(c) + "\n")
                code[0] = 1
        except BaseException as e:  # noqa: BLE001
            # 채점기 내부 프레임은 숨기고 solution.py 부분만 보여준다
            te = traceback.TracebackException.from_exception(e)
            frames = [f for f in te.stack if f.filename == "solution.py"]
            if frames:
                te.stack = traceback.StackSummary.from_list(frames)
            sys.stderr.write("".join(te.format()))
            code[0] = 1

    threading.stack_size(STACK)
    t = threading.Thread(target=body)
    t.start()
    t.join()
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(code[0])


if __name__ == "__main__":
    path = sys.argv[1]
    sys.argv = ["solution.py"]
    main(lambda: run(path, new_module("__main__")))
