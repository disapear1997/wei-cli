from wei.intents.doctor.normal import doctor

def register_doctor(subparsers):
    # wei docker
    doctor_parser = subparsers.add_parser("doctor",help="doctor tool")
    doctor_parser.set_defaults(func=doctor)