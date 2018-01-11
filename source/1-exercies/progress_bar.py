# Print iterations progress

import sys

# Usage in-code:
# import progress_bar
# progress_bar.print_progress_bar(0, 200, 'Progress:', 'Complete', 5)
# for x in range(0,100):
#    sleep(0.01)
#    progress_bar.print_progress_bar(x, 200, 'Progress:', 'Complete', 5)


def print_progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '0'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total:
        print
