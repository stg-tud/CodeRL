#
# Copyright (c) 2022, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#

import io

from datasets.reindent import run as run_reindent


def reindent_code(codestr):
    """
    Given code string, reindent it in the same way that the
    GitHub dataset was indented
    """
    codestr = io.StringIO(codestr)
    ret = io.StringIO()

    run_reindent(
        codestr,
        ret,
        config={
            "dry-run": False,
            "help": False,
            "to": 4,
            "from": -1,
            "tabs": True,
            "encoding": "utf-8",
            "is-tabs": False,
            "tabsize": 4,
            "all-tabs": False
        }
    )

    return ret.getvalue()


def get_error_type(result, binary=False):
    # binary classification critic 
    if binary:
        if result is True:
            return 1
        else:
            return 0

    # Compile error 
    if result == -2:
        return 0
    # Runtime error
    elif result == -1:
        return 1
    # Failed unit tests 
    elif result is False:
        return 2
    # Passed all unit tests
    elif result is True:
        return 3
    else:
        raise NotImplementedError(f"{result=}")


def get_reward_from_error_type(error_type):
    if error_type == 0:
        # Compile error
        return -1
    elif error_type == 1:
        # Runtime error
        return -0.6
    elif error_type == 2:
        # Failed unit tests
        return -0.3
    elif error_type == 3:
        # Passed all unit tests
        return 1
    else:
        raise NotImplementedError(f"{error_type=}")
