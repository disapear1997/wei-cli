from wei.intents.dev.version import VersionManager

def patch(args):
    return VersionManager().patch()


def register_dev(subparsers):
    # wei dev
    dev_parser = subparsers.add_parser("dev",help="Developer tools")    
    dev_subparsers = dev_parser.add_subparsers()

    # wei dev version
    version_parser = dev_subparsers.add_parser("version",help="Project version tools")
    version_subparsers = version_parser.add_subparsers()

    # wei dev version patch
    patch_parser = version_subparsers.add_parser("patch",help="Increase patch version")
    patch_parser.set_defaults(func=patch)