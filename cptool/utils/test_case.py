from pathlib import Path
from typing import List, Optional


class TestCase:
    def __init__(self, inp: Path, ok: Optional[Path]):
        self.inp = inp
        self.ok = ok
        self.ans: List[Path] = []

    def add_ans(self, ans: Path):
        self.ans.append(ans)

    def diff(self):
        flag = self._read(self.ok if self.ok else self.ans[0])
        results = []

        for file in self.ans[1:]:
            content = self._read(file)
            if content != flag:
                results.append(str(file))

        if results:
            return str(self.ok if self.ok else self.ans[0]), results
        return None

    def _read(self, file: Path):
        with file.open("r") as f:
            return f.read().strip()
