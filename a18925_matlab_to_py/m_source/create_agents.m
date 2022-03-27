function [agent]=create_agents(nr,ng)

 %creates the objects representing each agent
 
%agent - cell array containing list of objects representing agents
%nr - number of red squirrels
%ng - number of grey squirrels

%global parameters
%ENV_DATA - data structure representing the environment (initialised in
%create_environment.m)
%MESSAGES is a data structure containing information that agents need to
%broadcast to each other
%PARAM - structure containing values of all parameters governing agent
%behaviour for the current simulation
 
 global ENV_DATA MESSAGES PARAM 
  
bm_size=ENV_DATA.bm_size;
rloc=(bm_size-1)*rand(nr,2)+1;      %generate random initial positions for red squirrels
gloc=(bm_size-1)*rand(ng,2)+1;      %generate random initial positions for grey squirrels

MESSAGES.pos=[rloc;gloc];

%generate all red squirrel agents and record their positions in ENV_MAT_R
for r=1:nr
    pos=rloc(r,:);
    %create red squirrel agents with random ages between 0 and 10 days and
    %food level 20
    age=ceil(rand*10);
    %food=ceil(rand*20)+20;
    food=20;
    lbreed=round(rand*PARAM.R_BRDFQ);
    agent{r}=red_squirrel(age,food,pos,PARAM.S_SPD,lbreed);
end

%generate all grey squirrel agents and record their positions in ENV_MAT_F
for f=nr+1:nr+ng
    pos=gloc(f-nr,:);
    %create grey squirrel agents with random ages between 0 and 10 days and 
    %food level 30
    age=ceil(rand*10);
    %food=ceil(rand*20)+20;
    food=30;
    lbreed=round(rand*PARAM.G_BRDFQ);
    agent{f}=grey_squirrel(age,food,pos,PARAM.S_SPD,lbreed);
end
