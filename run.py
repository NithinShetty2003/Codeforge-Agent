from agent.benchmark import run_benchmark

test_cases = {}

with open("examples/sql_injection.py") as f:
    test_cases["SQL Injection"] = f.read()

with open("examples/buggy_flask.py") as f:
    test_cases["Buggy Flask"] = f.read()

with open("examples/inefficient_algo.py") as f:
    test_cases["Inefficient Algo"] = f.read()

results = run_benchmark(test_cases)

for r in results:
    print("="*50)
    print("Test Case:", r["test_case"])
    print("Score:", r["score"])
    print("Analysis:", r["analysis"])