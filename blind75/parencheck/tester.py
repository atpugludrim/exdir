from __future__ import print_function
import os
import argparse
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-n","--number_test_cases",default=100,type=int)
    args = parser.parse_args()
    os.system("python3 testcase_generator.py -n {}".format(args.number_test_cases))
    os.system("python3 parentheses_checker.py < cases.txt > outputs.txt")
    with open("groundtruth.txt","r") as f:
        trues = f.readlines()
    with open("outputs.txt","r") as f:
        preds = f.readlines()
    ctr = 0
    for idx,(ci,cj) in enumerate(zip(trues,preds),1):
        if ci.strip()!=cj.strip():
            print("Mismatch found at case number: {} [expected: {} program output: {}]".format(idx,ci,cj))
            ctr += 1
    print("{}/{} mismatches found".format(ctr,idx))
    os.remove("cases.txt")
    os.remove("groundtruth.txt")
    os.remove("outputs.txt")
if __name__=="__main__":
    main()
