#!/usr/bin/env python3

import unittest


def main():
    """Run the script only if unittest on yaml passes"""
    my_unittest = unittest.main(module='yaml_test', exit=False)
    if not my_unittest.result.failures:
        print('Do something')


if __name__ == '__main__':
    main()
