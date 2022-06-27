import random
import argparse
def create_false_case(_len):
    false_case_alph = ["{","[","(","}","]",")"]
    case = []
    for i in range(_len):
        idx = random.randint(0,len(false_case_alph)-1)
        case.append(false_case_alph[idx])
    return "".join(case)
def create_true_case(_len):
    alphabet = ["{","[","("]
    match = {"{":"}","[":"]","(":")"}
    if _len % 2 != 0:
        _len += 1
    case = []
    stack = []
    for i in range(_len):
        if len(stack) == (_len - i):
            case.append(match[stack.pop()])
        # if stack len doesn't exceed remaining len
        # either open new random, or close from stack
        else:
            TorF = random.random() > 0.8 # HOW DOES THIS NUMBER AFFECT THE GENERATED CASES?
            if TorF and len(stack) > 0: # if this number is small, there's higher chance of it being true, therefore more often it'll close old sequences therefore it will result in shorter parentheses sequences, little nesting.
            # case 1
                case.append(match[stack.pop()])
            else:
                idx = random.randint(0, len(alphabet)-1)
                case.append(alphabet[idx])
                stack.append(alphabet[idx])
    return "".join(case)
def create_case(max_len):
    sample_len = random.randint(0,max_len)
    TorF = random.random() > 0.5
    if TorF:
        return create_true_case(sample_len), True
    else:
        return create_false_case(sample_len), False
def create_test(args):
    n = args['n']
    max_len = args['max_len']
    output_file = args['output_file']
    ground_truth = args['ground_truth']
    labels = []
    with open(output_file,"w") as f:
        f.write("{}\n".format(n))
        for i in range(n):
            case, label = create_case(max_len)
            f.write("{}\n".format(case))
            labels.append(label)
    with open(ground_truth,"w") as f:
        f.write("\n".join([str(l) for l in labels]))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",default=100,type=int)
    parser.add_argument("--max-len","-ml",default=int(1e4),type=int)
    parser.add_argument("--output-file","-o",default="cases.txt")
    parser.add_argument("--ground-truth","-g",default="groundtruth.txt")
    args = parser.parse_args()
    create_test(vars(args))
if __name__=="__main__":
    main()
