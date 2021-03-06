#!/usr/bin/env python

import sys

def main(argv):
    # fixup_info.py Info.plist "quodlibet" "Quod Libet" "3.4.0"

    with open(argv[1], "rb") as h:
        data = h.read()

    app_id = argv[2]
    app_name = argv[3]
    app_version = argv[4]

    data = data.replace(">Application<", ">%s<" % app_name)
    data = data.replace("@APP_ID@", app_id)
    data = data.replace(">_launcher<", ">%s<" % app_id)
    data = data.replace("@APP_VERSION@", app_version)

    with open(argv[1], "wb") as h:
        h.write(data)

if __name__ == "__main__":
    main(sys.argv)
