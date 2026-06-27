from wei.intents.docker.normal import docker_enter

def register_docker(subparsers):
    # wei docker
    docker_parser = subparsers.add_parser("docker",help="docker tool")    
    docker_subparsers = docker_parser.add_subparsers()

    # wei docker enter
    enter_parser = docker_subparsers.add_parser("enter",help="enter the docker container")
    enter_parser.set_defaults(func=docker_enter)