# competitive-programming-toolkit

```
usage: cptool [-h] [--create PROBLEM_NAME] [--testgen NUMBER_OF_TEST_CASE]
              [--test] [--diff FILES [FILES ...]]

A toolkit for Competitive Programming

optional arguments:
  -h, --help            show this help message and exit
  --create PROBLEM_NAME
                        create a new problem from a sample template
  --testgen NUMBER_OF_TEST_CASE
                        generate a number of test cases based on your
                        logic/logic.py
  --test                test your codes on test cases
  --diff FILES [FILES ...]
                        show different between *.ans files
```

## Install

```bash
https://github.com/ndtho8205/competitive-programming-toolkit.git
cd competitive-programming-toolkit
./install.sh
```

The script just simply create a hard link between `cptool.py` and `~/.local/bin/cptool`. You will need to add `~/.local/bin` to your `$PATH`.
