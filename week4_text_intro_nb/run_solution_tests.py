# run_solution_tests.py — run tests against solutions by aliasing them as student.*
import os, sys, types, importlib.util, unittest, pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))                # make tests/ importable
tests_dir = HERE / "tests"
(tests_dir / "__init__.py").touch(exist_ok=True)
os.chdir(HERE)                                # anchor discovery here

# Create a virtual 'student' package that points to solutions/*
if "student" not in sys.modules:
    sys.modules["student"] = types.ModuleType("student")

solutions_dir = HERE / "solutions"
for py in solutions_dir.glob("*.py"):
    stem = py.stem                      # e.g., homework
    mod_name = f"student.{stem}"        # tests import student.homework
    spec = importlib.util.spec_from_file_location(mod_name, str(py))
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader, f"Cannot load {py}"
    spec.loader.exec_module(mod)
    sys.modules[mod_name] = mod

suite = unittest.defaultTestLoader.discover("tests", pattern="test*.py")
unittest.TextTestRunner(verbosity=2).run(suite)
