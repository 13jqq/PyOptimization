import os
import fnmatch
import platform
import configparser


def merge_files(root, pattern, ext, lines, sort):
    filenames = []
    for filename in os.listdir(root):
        path = os.path.join(root, filename)
        if os.path.isdir(path):
            merge_files(path, pattern, ext, lines, sort)
        elif fnmatch.fnmatch(filename, pattern):
            filenames.append(filename)
    if filenames:
        try:
            if sort:
                filenames.sort(key=lambda filename: int(os.path.splitext(os.path.basename(filename))[0]))
        except:
            print('Sort failed')
        pathMerge = root + ext
        print(pathMerge)
        fMerge = open(pathMerge, 'w')
        for filename in filenames:
            path = os.path.join(root, filename)
            f = open(path, 'r')
            data = f.read()
            f.close()
            fMerge.write(data + ''.join(['\n'] * lines))
        fMerge.close()


def main():
    config = configparser.ConfigParser()
    config.read(os.path.splitext(__file__)[0] + '.ini')
    name = os.path.splitext(os.path.basename(__file__))[0]
    merge_files(
        os.path.expandvars(config.get(name, 'root.' + platform.system())),
        config.get(name, 'pattern'),
        config.get(name, 'ext'),
        config.getint(name, 'lines'),
        config.getboolean(name, 'sort'),
    )


if __name__ == '__main__':
    main()
