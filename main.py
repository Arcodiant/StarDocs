from pkg_resources import packaging
import logging

log = logging.getLogger("mkdocs.starDocs")

def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def version_check(version):
        if packaging.version.parse(version) < packaging.version.parse("3.24.3"):
            log.warning("Doc file '"+env.page.file.src_uri+"' failed version check with " + version)
            return "!!! danger inline end \"Last Updated\"\n    Alpha "+version+"\n\n    Information on this page may be outdated."
        else:
            return "!!! success inline end \"Last Updated\"\n    [Alpha "+version+"](https://robertsspaceindustries.com/comm-link/Patch-Notes/20309-Star-Citizen-Alpha-3243)"