import os

def get_short_path(cwd):
    home = os.getenv('HOME')
    names = cwd.split(os.sep)
    if names[0] == '': names = names[1:]
    path = ''
    for i in range(len(names)):
        path += os.sep + names[i]
        if os.path.samefile(path, home):
            return ['~'] + names[i+1:]
    return names


def add_cwd_segment():
    cwd = powerline.cwd or os.getenv('PWD')
    names = get_short_path(cwd.decode('utf-8'))

    max_depth = powerline.args.cwd_max_depth
    # better to try using xwininfo to get actual width
    # only issue here is that you may not always be using X (e.g. SSH, will need to test)
    # xwininfo -id (xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}') | grep --color=never geometry | grep -Eo "[0-9]*x[0-9]*"'
    if len(names) > max_depth:
        names = names[0] + [u'\u2026'] + names[-1]

    if not powerline.args.cwd_only:
        names[0] = ' /'+names[0]
        for n in names[:-1]:
            powerline.append('%s/' % n, Color.PATH_FG, Color.PATH_BG,
                    powerline.separator_thin, Color.SEPARATOR_FG)
    powerline.append('%s ' % names[-1], Color.CWD_FG, Color.PATH_BG)

add_cwd_segment()
