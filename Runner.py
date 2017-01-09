import subprocess32

def prepParams(bin, perf, test):
    if perf == 0:
        return ["scripts/runTest", "run", "-bf", bin, "-pa", test[1], "-in", test[2], "-ou", test[3], "-t", test[4], "-m", test[5]]
    else:
        return ["scripts/runTest", "run", "-bf", bin, "-p", "aaa", "-pa", test[1], "-in", test[2], "-ou", test[3], "-t", test[4], "-m", test[5]]

tests = ["/home/jan/a.out", 0,
         [3,"params", "/home/jan/in", "/home/jan/out", "10", "100000"],
         [3, "params", "/home/jan/in", "/home/jan/out", "0", "100000"],
         [3, "params", "/home/jan/in", "/home/jan/out", "10", "0"]]


for test in tests[2:]:
    clkTick = []
    perfs = []
    times = []
    mems = []
    diffs = []
    exs = []
    for i in range(0, test[0]):
        subprocess32.call(prepParams(tests[0], tests[1], test))
        f=open("stat.stat")
        values=f.readline().split(";")
        f.close()
        clkTick += [values[0]]
        perfs += [values[1]]
        times += [values[2]]
        mems += [values[3]]
        diffs += [values[4]]
        exs += [values[5]]
    print clkTick
    print perfs
    print times
    print mems
    print diffs
    print exs





