def agnt_solve(agent=None, *args, **kwargs):
    varargin = agnt_solve.varargin
    nargin = agnt_solve.nargin

    # sequence of functions called to apply agent rules to current agent population.
    ############
    # [nagent,nn]=agnt_solve(agent)
    ###########
    # agent - list of existing agent structures
    # nagent - list of updated agent structures
    # nn - total number of live agents at end of update

    # Created by Dawn Walker 3/4/08

    n = length(agent)
    # agnt_solve.m:13

    n_new = 0
    # agnt_solve.m:14

    prev_n = copy(n)
    # agnt_solve.m:15

    # execute existing agent update loop
    for cn in arange(1, n).reshape(-1):
        curr = agent[cn]
        # agnt_solve.m:19
        if logical_or(isa(curr, "red_squirrel"), isa(curr, "grey_squirrel")):
            curr, eaten = eat(curr, cn, nargout=2)
            # agnt_solve.m:21
            if eaten == 0:
                curr = migrate(curr, cn)
            # agnt_solve.m:23
            curr, klld = die(curr, cn, nargout=2)
            # agnt_solve.m:25
            #         if klld==0
            #             new=[];
            #             [curr,new]=breed(curr,cn);			#breeding rule
            #             if ~isempty(new)					#if current agent has bred during this iteration
            #                  n_new=n_new+1;                 #increase new agent number
            #                  agent{n+n_new}=new;			#add new to end of agent list
            #              end
            #         end
            agent[cn] = curr
    # agnt_solve.m:34

    temp_n = n + n_new
    # agnt_solve.m:38

    nagent, nn = update_messages(agent, prev_n, temp_n, nargout=2)


# agnt_solve.m:39
