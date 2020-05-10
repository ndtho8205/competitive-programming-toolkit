# competitive-programming-toolkit

```bash
usage: cptool [-h] [-v] [SUBCOMMAND] ...

A simple toolkit for Competitive Programming

positional arguments:
  [SUBCOMMAND]
    new          Create a new problem.
    scrape       Scrape problem url.
    check        Check the validity of the `project.toml` file.
    testgen      Generate a number of test cases using your
                 testgen/generator.py implementation.
    test         Test your codes on test cases.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  print version info
```

## Install

Install via pip:

```bash
pip install git+https://github.com/ndtho8205/competitive-programming-toolkit.git
```

Install via pipx (recommended):

```bash
pipx install git+https://github.com/ndtho8205/competitive-programming-toolkit.git
```

## Usage

1. Create a new problem named `problem_1`

   ```bash
   $ cptool new problem_1

   $ tree problem_1
   problem_1
   ├── codes            <--- your codes go here
   ├── problem.yaml     <--- problem statements
   ├── README.md
   └── test_cases       <--- all test cases go here
       ├── examples
       ├── generated
       ├── handmade
       └── generator.py <--- function `generate` in this file must be implemented first.
                             `cptool` use this file to automatically generate test cases.

   $ cat problem_1/test_cases/generator.py
   ───────┬──────────────────────────────────────────────────────────────────
          │ file: test_cases/generator.py
   ───────┼──────────────────────────────────────────────────────────────────
     1    │ from typing import Callable
     2    │
     3    │ # min_n = 1
     4    │ # max_n = 1000000
     5    │
     6    │
     7    │ def generate(f_rand: Callable[[int, int], int]):
     8    │     # f_rand(min_range, max_range) is a function
     9    │     # that return a pesudo-random integer
     10   │     # in [min_range, max_range]
     11   │     # print(f_rand(min_range=min_n, max_range=max_n))
     12   │     raise NotImplementedError()
     13   │
     14   │
     15   │ if __name__ == "__main__":
     16   │     generate(f_rand=lambda x, y: 3)
   ───────┴──────────────────────────────────────────────────────────────────
   ```

2) Solve the problem and save all your codes in `code` directory

   You should prepare at least two different solutions, so that you can compare
   their outputs to find out any problems in your codes.

3) Implement `generate` function in `test_cases/generator.py`

   You should use `f_rand` function provided by `cptool` to correctly create
   randomized test cases.

4) Prepare test cases by yourself or using `cptool`

   ```bash
   $ cd problem_1
   $ cptool testgen 4
   Generating test cases in `target/generated`
   Successfully generated 4 test cases

   $ tree target/generated
   test/generated
   ├── 00.in
   ├── 01.in
   ├── 02.in
   ├── 03.in
   └── 04.in
   ```

5. Test your codes

   ```bash
   $ cd problem_1
   $ cptool test       <--- outputs from your code are stored at `target/`

   Successfully compiled file `codes/problem1_1.cpp` in `target/codes/problem1_1`
   Successfully compiled file `codes/problem1_2.cpp` in `target/codes/problem1_2`

   Running your code on sample test cases
     1 test cases are tested.
     ✅ There are no differences among your codes' outputs :)
   Running your code on handmade test cases
     2 test cases are tested.
     ✅ There are no differences among your codes' outputs :)
   Running your code on generated test cases
     4 test cases are tested.
     ✅ There are no differences among your codes' outputs :)

   $ tree target
     target
     ├── codes                        <--- compiled and executable codes go here
     │   ├── problem1_1
     │   └── problem1_2
     └── test
         ├── generated
         │   ├── 00_problem1_1.ans   <--- outputs from your code is named following the pattern: *.ans
         │   ├── 00_problem1_2.ans        [problem_idx]_[code_filename].ans
         │   ├── 01_problem1_1.ans
         │   ├── 01_problem1_2.ans
         │   ├── 02_problem1_1.ans
         │   ├── 02_problem1_2.ans
         │   ├── 03_problem1_1.ans
         │   ├── 03_problem1_2.ans
         │   ├── 04_problem1_1.ans
         │   └── 04_problem1_2.ans
         ├── handmade
         └── sample
             ├── 01_problem1_1.ans
             └── 01_problem1_2.ans

   ```

6. Fix bugs

## Additional Features

- [WIP] Retrieve problem information (statement, input and output constraints,
  etc.) from URL. Supported sites: CodeChef.
- [WIP] Problem information is saved in `problem.yaml` which can be further
  export to different format such as Markdown, LaTeX, etc.
