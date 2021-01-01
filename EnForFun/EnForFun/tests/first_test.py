def function_1(var):
  return var + 1

def test_success():
  assert function_1(4) == 5

def test_failure():
  assert function_1(2) == 5
