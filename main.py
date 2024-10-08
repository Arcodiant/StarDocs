from pkg_resources import packaging

def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def version_check(version):
        if packaging.version.parse(version) < packaging.version.parse("3.24.1"):
            return "!!! danger inline end \"Last Updated\"\n    Alpha "+version+"\n\n    Information on this page may be outdated."
        else:
            return "!!! success inline end \"Last Updated\"\n    [Alpha "+version+"](https://robertsspaceindustries.com/comm-link/transmission/19985-Alpha-324-Cargo-Empires)"