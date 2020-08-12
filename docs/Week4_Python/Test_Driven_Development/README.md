# TDD - Test Driven Development :hammer_and_wrench:

## What is TDD?
- TDD is the process of developing and running automated test before actual development of the application.
- Relies on the repetition of a very short development cycle.
- Sometimes called **Test First Development**
- The tests **drive** development

## Why do we use TDD?
- Reduces the number of bugs when applied to legacy projects 
- Decreases bug to code ratio in new projects 
- Increases overall software quality.
- Increases code quality.
- TDD is one of the common practices of Agile core development.
- Agile is feedback driven development and **feedback is critical**
- Requirements you start with may change during development cycle


## Benefits of using TDD
* **Early bug notification**
    - Developers can test their code but in the database world, this often consists of manual tests or one-off scripts.
    - Using TDD, you can build up, over time, a suite of automated tests that you and other developers can rerun.

* **Better Designed, cleaner and more extensible code**
    - Helps to understand how the code will be used and how it interacts with other modules.
    - Better design decision, maintainable code.
    - TDD allows writing smaller code having responsibility rather than monolithic procedures with multiple responsibilities.
    - TDD forces to write only production code to pass tests based on user requirements.
    
* **Confidence to Refactor**
    - When refactoring code, there is a greater likelihood of breaks.
    - Having set of automated tests can fix those breaks before release.
    - Proper warning is given when breaks are identified.

## Limitations of TDD
- Large numbers of **unit tests** can become hard to maintain as the project grows in size.

## TDD in Agile 
- Development technique where you must first write a test that fails before you write new functional code. 
- Starts with designing and developing tests for every small functionality and prompts developers to write new code only if an automated test has failed. 
 

## Using Pytest 

**Installing pytest**

```bash
$ python -m pip install pytest
```

The test file **must** include key word **test**
```bash
calc_test
```

**An examples of a simple test:**

```python
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

**To execute it:**

```python
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-5.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```