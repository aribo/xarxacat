from fabric.api import *
from fabric.colors import green, red


# Simple git workflow, where you are merging local feature branches into remote branches.(from: http://www.yaconiello.com/blog/deploying-django-site-fabric/)

def build_commit(warn_only=True):
    """Build a commit"""
    local_branch = prompt("checkout branch: ")
    rebase_branch = prompt("rebase branch: ")

    local('git checkout %s' % local_branch)
    local('git add .')
    local('git add -u .')

    message  = prompt("commit message: ")

    local('git commit -m "%s"' % message)
    local('git checkout %s' % rebase_branch)
    local('git pull origin %s' % rebase_branch)
    local('git checkout %s' % local_branch)
    local('git rebase %s' % rebase_branch)
    local('git checkout %s' % rebase_branch)
    local('git merge %s' % local_branch)
    local('git push origin %s' % rebase_branch)
    local('git checkout %s' % local_branch)