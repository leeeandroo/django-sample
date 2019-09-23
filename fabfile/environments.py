import json

from fabric.api import env

with open("etc/deploy.json") as handle:
    config = json.load(handle)

env.use_ssh_config = True
env.git_url = config["deploy"]["giturl"]


def testing():
    """Testing environment."""
    env.env_type = "testing"
    env.forward_agent = True
    env.roledefs = {
        "sample.gui": config["testing"]["server"]
    }
    env.base_dir = config["testing"]["basedir"].format(config)
    env.releases = "{}/releases".format(env.base_dir)
    env.current = "{}/current".format(env.base_dir)
    env.user = config["testing"]["user"]
    env.port = config["testing"]["port"]
    env.git_branch = config["testing"]["gitbranch"]


def production():
    """Production environment."""
    env.env_type = "production"
    env.forward_agent = True
    env.roledefs = {
        "sample.gui": config["production"]["server"]
    }
    env.base_dir = config["production"]["basedir"].format(config)
    env.releases = "{}/releases".format(env.base_dir)
    env.current = "{}/current".format(env.base_dir)
    env.user = config["production"]["user"]
    env.port = config["production"]["port"]
    env.git_tag = config["production"]["gittag"]