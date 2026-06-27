from wei.intents.git.normal import git_sync

def register_git(subparsers):
    # wei sync
    git_parser = subparsers.add_parser("git",help="git tool")    
    git_subparsers = git_parser.add_subparsers()

    # wei git sync
    sync_parser = git_subparsers.add_parser("sync",help="sync now folder to remote")
    sync_parser.add_argument("message",help="Git commit message")
    sync_parser.set_defaults(func=git_sync)