def breed(agt=None,cn=None,*args,**kwargs):
    varargin = breed.varargin
    nargin = breed.nargin

    #breeding function for class RED_SQUIRREL
#agt=red_squirrel object
#cn - current agent number
#new - contains new  agent object if created, otherwise empty
    
    global PARAM,IT_STATS,N_IT
    #N_IT is current iteration number
#IT_STATS is data structure containing statistics on model at each
#iteration (no. agents etc)
#PARAM is data structure containing migration speed and breeding
#frequency parameters for both foxes and rabbits
    
    flim=PARAM.R_FOODBRD
# breed.m:15
    
    tlim=PARAM.R_BRDFQ
# breed.m:16
    
    cfood=agt.food
# breed.m:17
    
    age=agt.age
# breed.m:18
    
    last_breed=agt.last_breed
# breed.m:19
    
    pos=agt.pos
# breed.m:20
    
    if cfood >= logical_and(flim,last_breed) >= tlim:
        new=red_squirrel(0,cfood / 2,pos,PARAM.S_SPD,0)
# breed.m:23
        agt.food = copy(cfood / 2)
# breed.m:24
        agt.last_breed = copy(0)
# breed.m:25
        agt.age = copy(age + 1)
# breed.m:26
        IT_STATS.div_red[N_IT + 1]=IT_STATS.div_red(N_IT + 1) + 1
# breed.m:27
    else:
        agt.age = copy(age + 1)
# breed.m:29
        agt.last_breed = copy(last_breed + 1)
# breed.m:30
        new=[]
# breed.m:31
    