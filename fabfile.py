from fabric.api import *
from fabric.colors import green, red





# Workflow to schemamigration data apps (source: http://stackoverflow.com/questions/3166284/django-south-creating-schemamigration-for-more-than-one-app)

APPS_TO_WATCH = ['assemblees','consell','membres', 'premsa']
def migration():
    for app in APPS_TO_WATCH:
        local('./ manage.py schemamigration %s --auto' % app)


# Simple git workflow, where you are merging local feature branches into remote branches.(source: http://www.yaconiello.com/blog/deploying-django-site-fabric/)

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