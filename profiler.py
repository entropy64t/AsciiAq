import os
import sys
import time
import importlib
from types import FunctionType
from functools import wraps
from typing import Any

class PerfTracker:
    """
    Tracks global execution time for all functions/methods in a directory.
    Automatically finds main.py, wraps it, and runs main.main().
    """

    def __init__(self):
        # fn_fullname -> [total_time, call_count]
        self.global_data = {}

    def track(self, fn: FunctionType, fullname: str = None) -> FunctionType:
        """Wrap a function or method to track execution time."""
        fn_name = fullname or fn.__qualname__

        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            elapsed = time.perf_counter() - start

            if fn_name not in self.global_data:
                self.global_data[fn_name] = [0.0, 0]
            self.global_data[fn_name][0] += elapsed
            self.global_data[fn_name][1] += 1

            return result

        return wrapper

    def track_module(self, module: Any):
        """Recursively wrap all functions and methods in a module."""
        for attr_name in dir(module):
            if attr_name.startswith("__"):
                continue
            attr = getattr(module, attr_name)

            # Module-level function
            if isinstance(attr, FunctionType):
                wrapped = self.track(attr, f"{module.__name__}.{attr.__name__}")
                setattr(module, attr_name, wrapped)

            # Class methods
            elif isinstance(attr, type):  # a class
                cls = attr
                for name, method in cls.__dict__.items():
                    if name.startswith("__"):
                        continue
                    if isinstance(method, (FunctionType, classmethod, staticmethod)):
                        # unwrap classmethod/staticmethod
                        if isinstance(method, (classmethod, staticmethod)):
                            orig_func = method.__func__
                        else:
                            orig_func = method
                        wrapped = self.track(orig_func, f"{cls.__name__}.{orig_func.__name__}")
                        # re-wrap as classmethod/staticmethod if needed
                        if isinstance(method, classmethod):
                            wrapped = classmethod(wrapped)
                        elif isinstance(method, staticmethod):
                            wrapped = staticmethod(wrapped)
                        setattr(cls, name, wrapped)

    def track_directory(self, path: str):
        """
        Track all Python files in a directory and auto-start main.py.
        """
        sys.path.insert(0, path)

        main_module = None

        for filename in os.listdir(path):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(module_name)
                    self.track_module(module)

                    if module_name == "main":
                        main_module = module
                except Exception as e:
                    print(f"Failed to import {module_name}: {e}")

        if main_module:
            if hasattr(main_module, "profile") and callable(main_module.profile):
                print("Starting main.profile() ...")
                main_module.profile()
            else:
                print("main.py found but no callable profile() function.")

    def report(self, report_name: str, top_n=50):
        s = report_name
        s += "\n=== GLOBAL FUNCTION AVERAGES ===\n"
        for fn_name, (total, count) in sorted(self.global_data.items(), key=lambda x: -x[1][0])[:top_n]:
            avg = total / count if count else 0
            s += f"{fn_name:50} called {count:8} times, avg {avg*1000:12.5f} ms, total {avg*count:8.3f} s\n"
        with open("report.txt", 'a') as report:
            report.write(s)

if __name__ == "__main__":
    tracker = PerfTracker()
    tracker.track_directory("src/game/")
    tracker.report("report")