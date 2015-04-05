#!/usr/bin/env python
import os
import sys

# http://ju.outofmemory.cn/entry/19802
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestRestFramework.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
