#! /usr/bin/python
# -*- coding:utf-8 -*-

class P1(object):
    def foo(self):
        print 'p1-foo'

class P2(object):
    def foo(self):
        print 'p2-foo'
    def bar(self):
        print 'p2-bar'

class C1(P2,P1):
    pass

class C2(P2,P1):
    def bar(self):
        print 'C2-bar'

class D(C2,C1):
    pass


if __name__ =='__main__':
    d=D()
    d.foo()
    d.bar()