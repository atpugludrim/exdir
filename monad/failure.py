class Failure:
    def __init__(this, value, failure=False, exc=None):
        this.value = value
        this.failed = failure
        this.exc = exc
    def bind(this, f):
        if this.failed:
            return Failure(None, True, this.exc)
        try:
            val = f(this.value)
            return Failure(val)
        except Exception as e:
            return Failure(None, True, e)
    def __repr__(this):
        return f" {this.value} failed: {this.failed} exc: {this.exc}"

def main():
    x = 65
    x = Failure(x).bind(chr)
    print(x)
    x = x.bind(ord).bind(lambda x: x + 12).bind(chr)
    print(x)
    x = x.bind(int)
    print(x)

if __name__=="__main__":
    main()
