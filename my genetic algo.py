import numpy as np
f=[0]*int(input("Enter no. of variable including the d value : "))
for i in range(len(f)):
    print("Enter value : ",end="")
    f[i]=int(input())
print(f)

n=int(input("Enter no. of chromosome/population : "))
print("Objective Function is : ",n)

ch=np.random.randint(0,30,(n,len(f)-1))
print("chromosomes \n",ch,"\n")

epoch=int(input("Enter no. of epoch required : "))

i=1
while i<=epoch:
    print("Epoch No. : ",i)
    
    # Computing the Fitness objective
    fit_obj=np.array([0.0]*ch.shape[0])
    for j in range(len(f)-1):
        fit_obj += f[j]*ch[:,j]
    fit_obj -=f[-1]
    print("Fitness object: ", fit_obj )
    
    # Computing the Fitness
    fit=1/(1+ fit_obj)
    print("Fitness : ",fit)
    
    # Calculating the probability
    prob = fit / fit.sum()
    print("Probability : ",prob)
    
    # Rollutte
    cum_prob = np.cumsum(prob)
    print("Cumulative prob : ",cum_prob)
    
    ran_num = np.random.random((ch.shape[0]))
    print("Random no. for cal Rollutte : ",ran_num)
    
    new_ch= np.zeros(ch.shape)
    
    for j in range(len(cum_prob)):
        for k in range(len(cum_prob)):
            if cum_prob[k] > ran_num[j]:
                new_ch[j,:] = ch[k,:]
                break
    print("new set of chromosomes \n", new_ch)

    # Crossover
    cr=np.random.random()
    print("Cross over rate : ",cr)

    cross_candid=[]

    for j in range(ch.shape[0]):
        if np.random.random() < cr:
            cross_candid+=[j]
    
    print("Candidate for crossover ",cross_candid)
    
    ch=new_ch.copy()
    
    for j in range(len(cross_candid)):
        len_ch=np.random.randint(0,ch.shape[1])
        ch[cross_candid[j],:]=list(new_ch[cross_candid[j],0:len_ch])+list(new_ch[cross_candid[(j+1)%len(cross_candid)],len_ch:])
    print("After Crossover \n",ch)

    # Mutation
    for j in range(int(np.random.random()*ch.size)):
        mut_no=np.random.randint(0,ch.size)
        row=mut_no//ch.shape[1]
        col=mut_no%ch.shape[1]
        ch[row,col]=np.random.randint(0,ch.size)
    print("After Mutation \n",ch)
    
    i+=1
    print("\n\n")
