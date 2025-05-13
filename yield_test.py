from contextlib import contextmanager

class MyError(Exception):
    pass

class MyError2(Exception):
    pass

@contextmanager
def try_catch():
    print "run command 1"
    print "run command 2"

    try:
        print "before yield"
        yield
        print "after yield"
    except MyError as e:
        print e
    else:
        print "run else block"

    print "end try catch"

@contextmanager
def wrap_try_catch():
    with(try_catch()):
        try:
            yield
        except MyError2 as e:
            print e

with(wrap_try_catch()):
    print "do somthing"
    # raise MyError("my error 1")
    raise MyError2("my error 2")
    print "end with"