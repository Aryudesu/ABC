import traceback


def d(record):
    traceback.format_exception(*record.exc_info)


def f():
    return 1/0


def g():
    return f()


try:
    g()
except:
    traceback.print_exc()
