#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   lib.py
@Desc    :   A lib file which contains the function could be reused 
@Time    :   2023/06/27 00:20:20
@Author  :   jackyliu16 <18922251299@163.com> 
@Version :   1.0
@Site    :   https://github.com/jackyliu16
"""

import os
import re
from typing import List


def get_file_list_with_pattern(root: str, pattern: str) -> List[str]:
    """
    Get a list of files in the directory that match the pattern.

    Args:
        root (str): The directory to search for files.
        pattern (str): The pattern to match.

    Returns:
        List[str]: A list of file paths that match the pattern.
    """
    files = []
    for file_name in os.listdir(root):
        if os.path.isfile(os.path.join(root, file_name)) and re.match(
            pattern, file_name
        ):
            files.append(os.path.join(root, file_name))
    return files
