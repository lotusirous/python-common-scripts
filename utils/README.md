
```py
import os
from subprocess import check_output, STDOUT, CalledProcessError
import shutil
import sys

def _execute_shell(cmd):
    status = False
    output = None
    try:
        output = check_output(cmd, stderr=STDOUT, shell=True, timeout=3, universal_newlines=True)
        status = True
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)

    return status, output


def traverse(loc):
    for dirpath, dirnames, filenames in os.walk(loc):
        for basename in filenames:
            yield basename, os.path.join(dirpath, basename)


def copy_file(src, dst):
    shutil.copy2(src, dst)


# Get current directory
working_dir = os.getcwd()


# Import file from a directory
sys.path.insert(0, '/path/to/application/app/folder')
import file
```