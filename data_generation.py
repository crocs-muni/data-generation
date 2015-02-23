__author__ = 'syso'
from bitarray import bitarray
from itertools import combinations
import random
import os

def All_var(F):
    all_vars = [];
    for i in range(len(F)):
        all_vars = all_vars + F[i];
    l = set(all_vars);
    return list(l);

def BFSAT(F):
    all_vars = All_var(F);
    res = [[],[]];
    for l in range(0, len(all_vars)+1):
        for s in combinations(all_vars, l):
            #print(s);
            val = 0;
            for i in range(len(F)):
                if(set.issubset(set(F[i]),s)):
                    val = val + 1 ;
            if(val % 2 == 1):
                res[1].append(s);
            else:
                res[0].append(s);
    return res;

def set_vars(barray, vars, val ):
    for i in range(len(vars)):
        barray[vars[i]] = val;
        #print(barray);
    return;

def generate(F, block_size, data_size, file, percentage = 1.0):
    func_settings = BFSAT(F);
    all_vars = All_var(F);

    #print(func_settings);
    #print(all_vars);
    for i in range(data_size//block_size):
        rbytes = os.urandom(block_size);
        #rbytes = bytearray(block_size);
        #print(rbytes);
        barray = bitarray();
        barray.frombytes(bytes(rbytes));
        #print(barray);
        if(random.random() <= percentage):
            res = 1;
        else:
            res = 0;
        vars = func_settings[res][random.randint(0,len(func_settings[res])-1)];
        print(vars);
        #print(all_vars);


        set_vars(barray,all_vars,0);
        set_vars(barray,vars,1);

        print(barray);
        barray.tofile(file);
    return ;


#Boolean function
F = [[0,1],[1,2],[2,3]];




outfile = open("data", "wb");
generate(F,1,10,outfile,1.0);






