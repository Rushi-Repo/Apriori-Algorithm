import sys
import time

file_csv = input('File Path (eg: Databases/1.csv)') #User denied file path (eg: Databases/1.csv)
minSup = float(input('Minimum Support:')) #User defined minimum support
minCon = float(input('Minimum Confidence:')) #User defined minimum confidence

with open(file_csv) as f: #Print the Transactional Inputs
    
    tran = 0
    db_trans = []
    
    for l in f:
        db_ = l.replace('\n', '').split(",")
        db_trans.append(db_)
    print('---------------Transactional Inputs---------------')
    while tran < len(db_trans):
        print(db_trans[tran])
        tran=tran+1

class Rule:

    def __init__(self, left, right, all):
        self.left = list(left)
        self.left.sort()
        self.right = list(right)
        self.right.sort()
        self.all = all

    def __hash__(self):

        return hash(str(self))
    
    def __str__(self):
        return ",".join(self.left)+" --> "+",".join(self.right) + " | "




def candidate_generation(gk):
    candidate_g_res = []
    len_gk = len(gk)

    i=0

    while i < len_gk:

        for j in range(i+1, len(gk)):
            num, num1 = gk[i], gk[j]
            n1, n2 = list(num), list(num1)
            n1.sort()
            n2.sort()
            if n1[:len(num)-1] == n2[:len(num)-1]:
                candidate_g_res.append(num | num1)
        
        i=i+1
    
    return candidate_g_res


def gen_FreqAndSupp():
    support = {}
    cand = [[]]
    gk = [[]]
    c_ = set()
    for t in db_trans:
        for item in t:
            c_.add(frozenset([item]))

    cand.append(c_)
    count = search(db_trans, c_)
    gk.append(list(count.keys()))
    support.update(count)

    k = 1
    while len(gk[k]) > 0:
        cand.append(candidate_generation(gk[k]))
        count = search(db_trans, cand[k+1])
        support.update(count)
        gk.append(list(count.keys()))
        k += 1
    return gk, support


def search(db_trans, chk):
    t=0
    count = {}
    for nb in chk:
        count[nb]=0
    for t in db_trans:
        for frequent_set in chk:
            if frequent_set.issubset(t):
                count[frequent_set] += 1
    n = len(db_trans)
    return {frequent_set: support/n for frequent_set, support in count.items() if support/n >= minSup}


def generate_sub_rule(frequent_sets, rights, a_res, support):
    right_size = len(rights[0])
    total_size = len(frequent_sets)
    if total_size-right_size > 0:
        rights = candidate_generation(rights)
        new_right = []
        for right in rights:
            left = frequent_sets - right
            if len(left) == 0:
                continue
            confidence = support[frequent_sets] / support[left]
            if confidence >= minCon:
                a_res.append([Rule(left, right, frequent_sets), support[frequent_sets],  confidence])
                new_right.append(right)

        if len(new_right) > 1:
            generate_sub_rule(frequent_sets, new_right, a_res, support)


def generate_rules(frequent, support):

    all_res = []
    i=2

    while i < len(frequent):
        if len(frequent[i]) == 0:
            break
        freq_sets = frequent[i]
        for frequent_sets in freq_sets:
            for right in [frozenset([val]) for val in frequent_sets]:
                left = frequent_sets-right
                confidence = support[frequent_sets] / support[left]
                if confidence >= minCon:
                    all_res.append([Rule(left, right, frequent_sets), support[frequent_sets], confidence])
        if len(freq_sets[0]) != 2:

            for frequent_sets in freq_sets:
                right = [frozenset([val]) for val in frequent_sets]
                generate_sub_rule(frequent_sets, right, all_res, support)
        i=i+1

    all_res.sort(key=lambda val: str(val[0]))
    return all_res


if __name__ == '__main__': #Printing the time taken
    prog_start_time_ = time.time()
    freq, s = gen_FreqAndSupp()
    res_val = generate_rules(freq, s)
    prog_end_time_ = time.time()
    print("\n---RULES---SUPPORT---CONFIDENCE:---")
    for r in res_val:
        a_ = str(r[0])
        a_r = str(r[1])
        a_r2 = str(r[2])
        print(a_, 'SUPPORT: '+a_r,"|", "CONFIDENCE: "+a_r2)
    print("\n-----------------------------------------------------------------------")
    print("TIME TAKEN:"+str(prog_end_time_ - prog_start_time_) + "s")
 

