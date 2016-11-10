# flake8: noqa


def iterate_promise(promise):
    if not promise.is_fulfilled:
        for foo in promise.future:
            yield foo
    assert promise.is_fulfilled
    return promise.get()
