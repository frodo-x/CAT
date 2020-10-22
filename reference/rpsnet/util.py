import os
import numpy as np

def get_best_model(task_search, checkpoint):
       
    log_files_a = os.listdir(checkpoint+"/")
    log_files_b = []

    for file in log_files_a:
        file_split = file.split(".")
        if(file_split[-1]=="txt"):
            file_split_2 = file_split[0].split("_")
            if(file_split_2[0]=="session" and file_split_2[1]==str(task_search)):
                log_files_b.append(file)
            
    best_acc = []
    best_acc_b = []
    for file in log_files_b:
        # print (file)
        try:
            f = np.loadtxt(checkpoint+"/"+file, skiprows=1)
            best_acc.append(max(f[-1,-1], f[-1,-2]) )
            best_acc_b.append(int(file.split("_")[2]))
        except:
            pass

    best_acc = np.array(best_acc)
    best_acc_b = np.array(best_acc_b)

    a = np.argmax(best_acc)
    print(best_acc[a], best_acc_b[a])
    return best_acc_b[a]


def is_all_done(task_search,q ,checkpoint):
    log_files_a = os.listdir(checkpoint+"/")
    log_files_b = []

    for file in log_files_a:
        file_split = file.split(".")
        if(file_split[-1]=="txt"):
            file_split_2 = file_split[0].split("_")
            if(file_split_2[0]=="session" and file_split_2[1]==str(task_search) ):
                log_files_b.append(file)

    best_acc = []
    best_acc_b = []
    for file in log_files_b:
        f = np.loadtxt(checkpoint+"/"+file, skiprows=1)
        print(len(f))
        if(len(f)!=q):
            return False
    return True




def get_path(L, M, N):
    path=np.zeros((L,M),dtype=float);
    for i in range(L):
        j=0;
        while j<N:
            rand_value=int(np.random.rand()*M);
            if(path[i,rand_value]==0.0):
                path[i,rand_value]=1.0;
                j+=1;
    return path;

def get_free_path(fixed_path):
    path = fixed_path.copy()*0
    c = 0
    for level in fixed_path:
        a = np.where(level==0)[0]
        if(len(a)>0):
            path[c,a[0]]=1
        c+=1
    return path



def flatten_list(a): return np.concatenate(a).ravel()








def print_model_report(model):
    print('-'*100)
    print(model)
    print('Dimensions =',end=' ')
    count=0
    for p in model.parameters():
        print(p.size(),end=' ')
        count+=np.prod(p.size())
    print()
    print('Num parameters = %s'%(human_format(count)))
    print('-'*100)
    return count

def human_format(num):
    magnitude=0
    while abs(num)>=1000:
        magnitude+=1
        num/=1000.0
    return '%.1f%s'%(num,['','K','M','G','T','P'][magnitude])

def print_optimizer_config(optim):
    if optim is None:
        print(optim)
    else:
        print(optim,'=',end=' ')
        opt=optim.param_groups[0]
        for n in opt.keys():
            if not n.startswith('param'):
                print(n+':',opt[n],end=', ')
        print()
    return

