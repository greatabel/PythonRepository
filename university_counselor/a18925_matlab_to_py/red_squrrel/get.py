def get(c=None,prop_name=None,*args,**kwargs):
    varargin = get.varargin
    nargin = get.nargin

    #standard function to allow extraction of memory parameters from rabbit object
    
    if 'age' == prop_name:
        val=c.age
# get.m:8
    else:
        if 'food' == prop_name:
            val=c.food
# get.m:10
        else:
            if 'pos' == prop_name:
                val=c.pos
# get.m:12
            else:
                if 'speed' == prop_name:
                    val=c.speed
# get.m:14
                else:
                    if 'last_breed' == prop_name:
                        val=c.last_breed
# get.m:16
                    else:
                        error('invalid field name')
    