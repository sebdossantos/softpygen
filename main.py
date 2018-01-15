import sys
import getopt

# instantiate the logger
from logging.config import fileConfig


class Main:
    def __init__(self):
        fileConfig('config/logger.ini')
        self.verbose = False

        # cmd args values
        self.cmd_a = ''
        self.cmd_b = ''

        # Boolean for run multiple cmd
        self.run_cmd_b = False
        self.run_cmd_c = False

    @staticmethod
    def usage():
        print 'main.py -h (or --help) => show accessible cmd lines'

    def start(self, input_args):
        long_args = ['help', 'cmd_a=', 'cmd_b=', 'cmd_c']
        short_args = 'ha:b:c'

        try:
            opts, args = getopt.getopt(input_args, short_args, long_args)
        except getopt.GetoptError as err:
            print str(err)
            self.usage()
            sys.exit(2)

        for o, a in opts:
            if o == '-v':
                self.verbose = True
            elif o in ('-h', '--help'):
                self.usage()
                sys.exit()
            elif o in ('-a', '--cmd_a'):
                self.cmd_a = a
            elif o in ('-b', '--cmd_b'):
                self.run_cmd_b = True
                self.cmd_b = a
            elif o in ('-c', '--cmd_c'):
                self.run_cmd_c = True
            else:
                assert False, 'unhandled option'

        # Run order when multiple command line
        if self.run_cmd_b:
            from display_log import display
            display()
        if self.run_cmd_c:
            # Do something
            pass


if __name__ == '__main__':
    m = Main()
    m.start(sys.argv[1:])
