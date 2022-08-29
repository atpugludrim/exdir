import os
import sys
import time
import signal

def sig_handler(signame):
    def sig_handler_(sig, frame):
        print("Caught {}".format(signame))
        sys.exit(sig)
    return sig_handler_

def main():
    for i in [x for x in dir(signal) if x.startswith("SIG")]:
        if not i.startswith("SIG_"):
            try:
                signum = getattr(signal, i)
                signal.signal(signum, sig_handler(i))
            except (OSError, RuntimeError, ValueError) as m:
                print("skipping {}".format(i))

    print(os.getpid())
    for _ in range(10 * 60):
        time.sleep(1)

if __name__=="__main__":
    main()
