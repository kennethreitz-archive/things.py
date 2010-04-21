from fabric.api import *

def test():
    """ Run nose/doc tests?
    """
    local("python ./tests/run_tests.py")

def init():
    """ Initialize a virtualenv in which to run tests against this
    """
    local("virtualenv .")
    local("pip install -E . fabric lxml nose opster")

def activate():
	""" Activate local virtualenv
	"""
	local("source ./bin/activate")

def clean():
    """ Remove the pycs
    """
    local("find . -name "*.pyc" -exec rm '{}' ';'")

def scrub():
    """
    Remove the cruft created by virtualenv and pip
    """
    local("rm -fr bin/ include/ lib/")