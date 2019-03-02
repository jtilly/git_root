# git_root
Find the root of a git repository (pilfered from https://stackoverflow.com/a/53675112)


## Installation
```shell
# pick one
pip install git+https://github.com/jtilly/git_root
conda install -c conda-forge git_root
pip install git_root
```


## Usage
```python
from git_root import git_root

git_root()
# /home/user/my_repo

git_root('dir1', 'file')
# /home/user/my_repo/dir1/file

git_root('dir1/file')
# /home/user/my_repo/dir1/file
```
