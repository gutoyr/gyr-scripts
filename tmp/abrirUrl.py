#!/usr/bin/env python

#def repo_paths():
#    import os, mercurial.hg, mercurial.ui
#    repo = mercurial.hg.repository(mercurial.ui.ui(), os.path.curdir)
#    return repo.ui.configitems('paths')
#
#def bitb_paths(paths):
#    import re
#    pattern = re.compile('bitbucket.org')
#    paths = [pattern.search(path) for name, path in paths]
#    return filter(None, paths)
#
#def open(paths):
#    import webbrowser
#    if paths:
#        url = 'http://' + paths[0].string[paths[0].start():]
#        webbrowser.open(url)
#    else:
#        raise Exception('BitBucket path not found')

#def main():
#    try:
#        open(bitb_paths(repo_paths()))
#    except Exception as err:
#        print 'abort:', err
def main():
    import webbrowser
    webbrowser.open('http://www.google.com')

if __name__ == '__main__':
    main()

