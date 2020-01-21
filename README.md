# competitive-programming-toolkit

```bash
usage: cptool [-h] [--create PROBLEM_NAME] [--testgen NUMBER_OF_TEST_CASE]
              [--test] [--diff FILES [FILES ...]]

A toolkit for Competitive Programming

optional arguments:
  -h, --help            show this help message and exit
  --create PROBLEM_NAME
                        create a new problem from a sample template
  --testgen NUMBER_OF_TEST_CASE
                        generate a number of test cases based on your
                        testgen/generator.py
  --test                test your codes on test cases
  --diff FILES [FILES ...]
                        show different between *.ans files
```

## Install

```bash
$ https://github.com/ndtho8205/competitive-programming-toolkit.git
$ cd competitive-programming-toolkit
$ ./install.sh
```

The script just simply creates a soft link between `cptool.py` and `~/.local/bin/cptool`. You will need to add `~/.local/bin` to your `$PATH`.

## Usage

1. Create a new problem named `problem_1`

  ```bash
  $ cptool --create problem_1
  Creating problem in problem_1
  Successfully created problem problem_1

  $ tree problem_1
  problem_1
  ├── code              <--- your code goes here
  ├── README.md
  ├── test              <--- all of your test cases go here
  │   ├── generated     <--- test cases generated by `cptool` go here
  │   ├── handmade      <--- test cases you prepared
  │   │   └── 01.in
  │   └── sample        <--- test cases including input and 100% correct output
  │       ├── 01.in     <--- *.in for input
  │       └── 01.ok     <--- *.ok for correct output
  └── testgen
      └── generator.py  <--- function `generate` in this file must be implemented first .
                            `cptool` use this file to automatically generate test cases.

  $ cat problem_1/testgen/generator.py
  ───────┬──────────────────────────────────────────────────────────────────
         │ File: testgen/generator.py
  ───────┼──────────────────────────────────────────────────────────────────
    1    │ from typing import Callable
    2    │
    3    │ # MIN_N = 1
    4    │ # MAX_N = 1000000
    5    │
    6    │
    7    │ def generate(f_rand: Callable[[], int]):
    8    │     # f_rand(min_range, max_range) is a function
    9    │     # that return a pesudo-random integer
    10   │     # in [min_range, max_range]
    11   │     # print(f_rand(min_range=MIN_N, max_range=MAX_N))
    12   │     raise NotImplementedError
    13   │
    14   │
    15   │ if __name__ == "__main__":
    16   │     generate(f_rand=lambda x, y: 3)
  ───────┴──────────────────────────────────────────────────────────────────
  ```

2. Solve the problem and save all your codes in `code` directory
   You should prepare at least two different solutions, so that you can compare their outputs to find out any problems in your code.

3. Implement `generate` function in `testgen/generator.py`
   You should use `f_rand` function provided by `cptool` to correctly create randomized test cases.

4. Prepare test cases by yourself or using `cptool`

  ```bash
  $ cd problem_1
  $ cptool --testgen 10
  Generating test cases in test/generated
  Successfully generated 10 test cases

  $ tree test/generated
  test/generated
  ├── 00.in
  ├── 01.in
  ├── 02.in
  ├── 03.in
  ├── 04.in
  ├── 05.in
  ├── 06.in
  ├── 07.in
  ├── 08.in
  └── 09.in
  ```

5. Test your codes

  ```bash
  $ cd problem_1
  $ cptool --test
  ```

6. Fix bug :laughing:
