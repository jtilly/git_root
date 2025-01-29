def git_root(*args):
    """Returns the root path of the git repository (without trailing slash). Any
    additional (and optional) arguments will be appended to the path.

    Examples
    ----------
    > git_root()
    /home/user/my_repo

    > git_root('dir1', 'file')
    /home/user/my_repo/dir1/file

    > git_root('dir1/file')
    /home/user/my_repo/dir1/file
    """
    import os
    import subprocess

    git_root = (
        subprocess.Popen(
            ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE
        )
        .communicate()[0]
        .rstrip()
        .decode("utf-8")
    )
    return os.path.abspath(os.path.join(git_root, *args))
