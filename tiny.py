import getopt
import perlpie
import os
import shutil
import sys

def tiny(projectname):
    shutil.rmtree('.git')
    os.remove('README')
    perlpie.listfiles('.', 'tiny', projectname)
    os.remove('perlpie.py')
    os.remove('perlpie.pyc')
    curdir = os.getcwd()
    newdir = curdir.replace('tiny', projectname)
    shutil.move(curdir, newdir)
    os.remove('tiny.py')

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    if len(args) < 1:
        print "Error: Missing project name"
        return
    # process arguments
    tiny(args[0]) # process() is defined elsewhere

if __name__ == '__main__':
    main()
