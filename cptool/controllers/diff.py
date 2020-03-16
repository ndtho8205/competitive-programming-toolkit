from typing import List
from pathlib import Path


def diff(output_path_list: List[Path]):
    # TODO: close after open
    # TODO: try other methods
    output_content_list = list(
        map(
            lambda output_path: "\n".join(open(output_path).readlines()),
            output_path_list,
        )
    )

    diff_list = []
    for i in range(0, len(output_path_list) - 1):
        for j in range(i + 1, len(output_path_list)):
            if output_content_list[i] != output_content_list[j]:
                diff_list.append((output_path_list[i].name, output_path_list[j].name))

    return diff_list
