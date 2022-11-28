from __future__ import annotations

import sys
from dataclasses import dataclass

from volosti_common.person.typedefs import (
    FullName,
    HashedPassword,
    ShortName,
    Username,
)

if sys.version_info < (3, 10):
    SLOTS = {}
else:
    SLOTS = {'slots': True}


@dataclass(**SLOTS)
class Account:
    username: Username
    hashed_password: HashedPassword
    profiles: list[Profile]


@dataclass(**SLOTS)
class Profile:
    short_name: ShortName
    full_name: FullName
