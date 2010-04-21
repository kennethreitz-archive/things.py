from fabric.api import *
# Server Stuff

# set(fab_user='alex', 
#      fab_hosts=['wincplace.com'], 
#      root='/sites/wincplace.com/httpdocs/', 
#      site='wincplace')
# 
# def deploy():
#     local('git archive --format=tar HEAD | gzip > $(site).tar.gz')
#     run('rm -rf $(root)$(site)') 
#     put('$(site).tar.gz', '$(root)$(site).tar.gz')
#     run('cd $(root)$(site) && tar zxf $(site).tar.gz')
#     restart()
# 
# def restart():
#     run('sh $(root)$(site)/restart.sh')


# Local Stuff




def dev():
	"""
	Run development server
	"""	
	local("python ./placehub/manage.py runserver")

def test():
    """
    Run nose tests?
    """
    local("python ./run_tests.py")

def init():
    """
    Initialize a virtualenv in which to run tests against this
    """
    local("virtualenv .")
    local("pip install -E . django django-piston django-mediasync fabric django-mongokit")

def activate():
	"""
    Activate local virtualenv
    """
	local("source ./bin/activate")

def cleanpip():
    """
    Remove the pycs
    """
    local("rm -fr *.pyc")

def cleanpip():
    """
    Remove the cruft created by virtualenv and pip
    """
    local("rm -fr bin/ include/ lib/")