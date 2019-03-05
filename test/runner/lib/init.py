"""Early initialization for ansible-test before most other imports have been performed."""

import resource

from lib.constants import (
    SOFT_RLIMIT_NOFILE,
)

CURRENT_RLIMIT_NOFILE = resource.getrlimit(resource.RLIMIT_NOFILE)
DESIRED_RLIMIT_NOFILE = (SOFT_RLIMIT_NOFILE, CURRENT_RLIMIT_NOFILE[1])

if DESIRED_RLIMIT_NOFILE < CURRENT_RLIMIT_NOFILE:
    resource.setrlimit(resource.RLIMIT_NOFILE, DESIRED_RLIMIT_NOFILE)
    CURRENT_RLIMIT_NOFILE = DESIRED_RLIMIT_NOFILE
