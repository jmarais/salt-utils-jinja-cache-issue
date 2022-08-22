import salt
import salt.client
import salt.version
import os
import logging
from pprint import pformat

logging.basicConfig(level=logging.DEBUG)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter("%(asctime)s %(name)s %(levelname)s:%(message)s")
c_handler.setFormatter(c_format)
logging.getLogger().addHandler(c_handler)
log = logging.getLogger(__name__)

log.info("start")

log.info("salt import version: %s", salt.version.__version__)


def main():
    m1_name = "crab"
    m2_name = "rock"

    cwd = os.getcwd()
    pillar_dir = os.path.join(cwd, "pillar")
    saltroot_dir = os.path.join(cwd, "saltroot")
    m1_config = os.path.join(cwd, m1_name + ".yaml")
    m2_config = os.path.join(cwd, m2_name + ".yaml")
    m1_cache_dir = os.path.join(cwd, "minion_cache", m1_name)
    m2_cache_dir = os.path.join(cwd, "minion_cache", m2_name)

    m1 = newMinion(m1_name, m1_config, m1_cache_dir, pillar_dir, saltroot_dir)
    result = m1.cmd("grains.items")
    log.debug("%s grains: %s", m1_name, pformat(result))

    m2 = newMinion(m2_name, m2_config, m2_cache_dir, pillar_dir, saltroot_dir)
    result = m2.cmd("grains.items")
    log.debug("%s grains: %s", m2_name, pformat(result))

    state_result = m1.cmd("state.sls", "manage_jinja", {"test": True}, full_return=True)
    log.debug("%s state_result: %s", m1_name, pformat(state_result))

    state_result = m2.cmd("state.sls", "manage_jinja", {"test": True}, full_return=True)
    log.debug("%s state_result: %s", m2_name, pformat(state_result))


def newMinion(name, minion_config, minion_cache_dir, pillarPath, saltRoots):
    if not os.path.exists(minion_cache_dir):
        os.makedirs(minion_cache_dir)
    opts = salt.config.minion_config(minion_config)
    saltenv = "base"
    pillar_roots = {saltenv: [pillarPath]}
    opts["id"] = name
    opts["file_client"] = "local"
    opts["saltenv"] = saltenv
    opts["state_top_saltenv"] = saltenv
    opts["file_roots"] = {saltenv: [saltRoots]}
    opts["pillar_roots"] = pillar_roots
    opts["root_dir"] = minion_cache_dir
    opts["cachedir"] = os.path.join(minion_cache_dir, "cache")
    opts["log_file"] = os.path.join(minion_cache_dir, "minion.log")
    opts["pidfile"] = os.path.join(minion_cache_dir, "salt-minion.pid")
    opts["pki_dir"] = minion_cache_dir
    opts["sock_dir"] = minion_cache_dir
    opts["utils_dirs"] = [os.path.join(minion_cache_dir, "extmods/utils")]
    opts["extension_modules"] = os.path.join(minion_cache_dir, "extmods")
    opts["default_include"] = ""
    opts["user"] = "salt_tester"

    client_caller = salt.client.Caller(mopts=opts)
    res = client_caller.cmd("saltutil.sync_all")
    log.debug("sync_modules: %s", pformat(res))
    return client_caller


if __name__ == "__main__":
    main()
