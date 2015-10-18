#!/usr/bin/env python
from unittest import main, TestCase
from assert_is import eq_, is_, is_int
from bug import debug, stack
from file import exists
from fixtures import error

class Test(TestCase):
    def test_bug(self):
        try:
            ererer
        except:
            bug=debug()
            is_(bug.e,Exception)
            eq_(bug.type,type(bug.e))
            eq_(bug.msg,str(bug.e))
            exists(bug.file)
            is_int(bug.line)

    def test_stack(self):
        try:
            error()
        except:
            for s in debug().stack:
                is_(s,stack)
                print s

if __name__ == "__main__": # pragma: no cover
    main()