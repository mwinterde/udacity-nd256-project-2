import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # Initialize empty file list
    files = []

    # Loop through list of files and directories
    for name in os.listdir(path):
        full_path = os.path.join(path, name)

        # If directory, make new call to find_files function
        if os.path.isdir(full_path):
            files.extend(find_files(suffix, full_path))
        # If file, append file path to result list
        else:
            if full_path.endswith(suffix):
                files.append(full_path)

    return files


def test():

    # Test 1
    results1 = [
        './testdir/subdir3/subsubdir1/b.c',
        './testdir/t1.c',
        './testdir/subdir5/a.c',
        './testdir/subdir1/a.c'
    ]
    assert find_files('.c', './testdir') == results1

    # Test 2
    results2 = [
        './testdir/subdir3/subsubdir1/b.h',
        './testdir/subdir5/a.h',
        './testdir/t1.h',
        './testdir/subdir1/a.h'
    ]
    assert find_files('.h', './testdir') == results2

    # Test 3
    results3 = []
    assert find_files('.exe', './testdir') == results3

    print("All tests successful")


if __name__ == '__main__':
    test()