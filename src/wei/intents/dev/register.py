from wei.intents.dev.version import VersionManager
from wei.intents.dev.install import dev_install

def patch(args):
    return VersionManager().patch()

def install(args):
    patch(args)
    dev_install(args)



def register_dev(subparsers):
    # wei dev
    dev_parser = subparsers.add_parser("dev",help="Developer tools")    
    dev_subparsers = dev_parser.add_subparsers()

    # wei dev install
    install_parser = dev_subparsers.add_parser("install",help="install wei (include change version auto)")
    install_parser.set_defaults(func=install)

    # wei dev version
    version_parser = dev_subparsers.add_parser("version",help="Project version tools")
    version_subparsers = version_parser.add_subparsers()

    # wei dev version patch
    patch_parser = version_subparsers.add_parser("patch",help="Increase patch version")
    patch_parser.set_defaults(func=patch)

    # wei dev version patch
    
    