# competitive-programming-toolkit
```bash
usage: cptool [-h] [-v] [SUBCOMMAND] ...

A toolkit for Competitive Programming

positional arguments:
  [SUBCOMMAND]
  new          Create a new problem.
  testgen      Generate a number of test cases using your
               testgen/generator.py implementation.
  test         Test your codes on test cases.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  print version info
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
$ cptool new problem_1
Creating problem in `problem_1`
Successfully created problem `problem_1`

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
    └── generator.py  <--- function `generate` in this file must be implemented first.
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
  7    │ def generate(f_rand: Callable[[int, int], int]):
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
$ cptool testgen 4
Generating test cases in `test/generated`
Successfully generated 4 test cases

$ tree test/generated
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
$ cptool test       <--- outputs from your code are stored at `temp/test`

Successfully compiled file `code/problem1_1.cpp` in `target/code/problem1_1`
Successfully compiled file `code/problem1_2.cpp` in `target/code/problem1_2`

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
  ├── code                        <--- compiled and executable codes go here
  │   ├── problem1_1
  │   └── problem1_2
  └── test
      ├── generated
      │   ├── 00_problem1_1.ans   <--- outputs from your code is named following the pattern:*.ans
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

6. Fix your bugs :laughing:
