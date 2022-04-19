import matplotlib.pyplot as plt


def plot_results(agent=None, nsteps=None, fmode=None, outImages=None, *args, **kwargs):
    varargin = plot_results.varargin
    nargin = plot_results.nargin

    # Plots 2d patch images of agents onto background
    ###########
    # plot_results(agent,nr,ng)
    ###########
    # agent - current list of agent structures
    # nr -  no. red squirrels
    # ng -  no. grey squirrels

    # Modified by D Walker 3/4/08

    global N_IT, IT_STATS, ENV_DATA, MESSAGES, CONTROL_DATA
    # declare variables that can be seen by all functions
    # N_IT is current iteration number
    # ENV_DATA - data structure representing the environment (initialised in
    # create_environment.m)
    # IT_STATS is data structure containing statistics on model at each
    # iteration (no. agents etc)
    # MESSAGES is a data structure containing information that agents need to
    # broadcast to each other

    # write results to the screen
    nr = IT_STATS.tot_red
    # plot_results.m:24
    ng = IT_STATS.tot_grey
    # plot_results.m:25
    disp(strcat("Iteration = ", num2str(N_IT)))
    disp(strcat("No. new red squirrels = ", num2str(IT_STATS.div_red(N_IT + 1))))
    disp(strcat("No. new grey squirrels = ", num2str(IT_STATS.div_grey(N_IT + 1))))
    disp(strcat("No. agents migrating = ", num2str(IT_STATS.mig(N_IT + 1))))
    disp(strcat("No. red squirrels dying = ", num2str(IT_STATS.died_red(N_IT + 1))))
    disp(strcat("No. grey squirrels dying = ", num2str(IT_STATS.died_grey(N_IT + 1))))
    disp(strcat("No. red squirrels total = ", num2str(nr(N_IT + 1))))
    disp(strcat("No. grey squirrels total = ", num2str(ng(N_IT + 1))))
    # plot line graphs of agent numbers and remaining food
    if (
        (fmode == false)
        or (N_IT == nsteps)
        or ((fmode == true) and (rem(N_IT, CONTROL_DATA.fmode_display_every) == 0))
    ):
        # Plotting takes time so fmode has been introduced to only plot every n=CONTROL_DATA.fmode_display_every iterations
        # This value increases with the number of agents (see ecolab.m L57-61) as plotting more agents takes longer.
        # fmode can be turned off in the command line - see ecolab documentation
        col[1] = "r-"
        # plot_results.m:42
        col[2] = "b-"
        # plot_results.m:43
        tot_food = IT_STATS.tfood
        # plot_results.m:45
        n = nr(N_IT + 1) + ng(N_IT + 1)
        # plot_results.m:46
        f2 = figure(2)
        # plot_results.m:47
        set(f2, "Units", "Normalized")
        set(f2, "Position", concat([0.5, 0.5, 0.45, 0.4]))
        subplot(3, 1, 1)
        cla
        subplot(3, 1, 1)
        plot((arange(1, N_IT + 1)), nr(arange(1, N_IT + 1)), col[1])
        axis_lim = max(ng, nr)
        # plot_results.m:53
        subplot(3, 1, 1)
        axis(concat([0, nsteps, 0, dot(1.1, max(axis_lim))]))
        subplot(3, 1, 2)
        cla
        subplot(3, 1, 2)
        plot((arange(1, N_IT + 1)), ng(arange(1, N_IT + 1)), col[2])
        subplot(3, 1, 2)
        axis(concat([0, nsteps, 0, dot(1.1, max(axis_lim))]))
        subplot(3, 1, 3)
        cla
        subplot(3, 1, 3)
        plot((arange(1, N_IT + 1)), tot_food(arange(1, N_IT + 1)), "m-")
        subplot(3, 1, 3)
        axis(concat([0, nsteps, 0, tot_food(1)]))
        subplot(3, 1, 1)
        title("No. live red squirrels")
        subplot(3, 1, 2)
        title("No. live grey squirrels")
        subplot(3, 1, 3)
        title("Total food")
        drawnow
        # create plot of agent locations.
        f3 = figure(3)
        # plot_results.m:67
        bm = ENV_DATA.bm_size
        # plot_results.m:69
        typ = MESSAGES.atype
        # plot_results.m:70
        clf
        set(f3, "Units", "Normalized")
        set(f3, "Position", concat([0.05, 0.05, 0.66, 0.66]))
        v = arange(1, bm)
        # plot_results.m:74
        X, Y = meshgrid(v, nargout=2)
        # plot_results.m:75
        Z = ENV_DATA.food
        # plot_results.m:76
        H = zeros(bm, bm)
        # plot_results.m:77
        hs = surf(Y, X, H, Z)
        # plot_results.m:78
        cm = colormap("summer")
        # plot_results.m:79
        icm = flipud(cm)
        # plot_results.m:80
        colormap(icm)
        set(hs, "SpecularExponent", 1)
        set(hs, "SpecularStrength", 0.1)
        hold("on")
        for cn in arange(1, length(agent)).reshape(-1):
            if typ(cn) > 0:
                pos = get(agent[cn], "pos")
                # plot_results.m:88
                if isa(agent[cn], "red_squirrel"):
                    ro = plot(pos(1), pos(2), "r.")
                    # plot_results.m:90
                    set(ro, "MarkerSize", 30)
                else:
                    fo = plot(pos(1), pos(2), ".", "Color", "#2c2e2c")
                    # plot_results.m:93
                    set(fo, "MarkerSize", 30)
        h = findobj(gcf, "type", "surface")
        # plot_results.m:99
        set(h, "edgecolor", "none")
        lighting("flat")
        h = findobj(gcf, "type", "surface")
        # plot_results.m:102
        set(h, "linewidth", 0.1)
        set(h, "specularstrength", 0.2)
        axis("off")
        axis("equal")
        set(gcf, "color", concat([1, 1, 1]))
        uicontrol(
            "Style",
            "pushbutton",
            "String",
            "PAUSE",
            "Position",
            concat([20, 20, 60, 20]),
            "Callback",
            "global ENV_DATA; ENV_DATA.pause=true; display(ENV_DATA.pause); clear ENV_DATA;",
        )
        while CONTROL_DATA.pause == true:

            pan("on")
            axis("off")
            title(
                concat(
                    ["Iteration no.= ", num2str(N_IT), ".  No. agents = ", num2str(n)]
                )
            )
            text(-2.6, 7.7, "PAUSED", "Color", "r")
            drawnow
            uicontrol(
                "Style",
                "pushbutton",
                "String",
                "ZOOM IN",
                "Position",
                concat([100, 20, 60, 20]),
                "Callback",
                "if camva <= 1;return;else;camva(camva-1);end",
            )
            uicontrol(
                "Style",
                "pushbutton",
                "String",
                "ZOOM OUT",
                "Position",
                concat([180, 20, 60, 20]),
                "Callback",
                "if camva >= 179;return;else;camva(camva+1);end",
            )
            uicontrol(
                "Style",
                "pushbutton",
                "String",
                "RESUME",
                "Position",
                concat([20, 20, 60, 20]),
                "Callback",
                "global ENV_DATA; ENV_DATA.pause=false; clear ENV_DATA;",
            )

        title(
            concat(["Iteration no.= ", num2str(N_IT), ".  No. agents = ", num2str(n)])
        )
        axis("off")
        drawnow
        if outImages == true:
            if fmode == true:
                disp(
                    "WARNING*** fastmode set - To output all Images for a movie, set fmode to false(fast mode turned off) "
                )
            filenamejpg = concat([sprintf("%04d", N_IT)])
            # plot_results.m:141
            eval(concat(["print -djpeg90 agent_plot_", filenamejpg]))

    return


if __name__ == "__main__":
    pass
