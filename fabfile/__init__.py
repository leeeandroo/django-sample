from fabric.api import roles

from .commands import deploy as _deploy
from .commands import rollback as _rollback
from .environments import production
from .environments import testing

__all__ = [
    "deploy",
    "production",
    "rollback",
    "testing"
]


@roles("sample.gui")
def deploy(branch=None):
    _deploy(branch=branch)


@roles("sample.gui")
def rollback():
    _rollback()
