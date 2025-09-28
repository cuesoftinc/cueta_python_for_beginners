# run_tests.py — always run tests against student/ code
import os, sys, unittest, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))               # make student/ importable
tests_dir = HERE / "tests"
(tests_dir / "__init__.py").touch(exist_ok=True)
os.chdir(HERE)                               # anchor discovery here
suite = unittest.defaultTestLoader.discover("tests", pattern="test*.py")
unittest.TextTestRunner(verbosity=2).run(suite)
