#!/usr/bin/env python
"""
Example of nested autocompletion.
"""
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
import os

completer = NestedCompleter.from_nested_dict(
{
    "activeUsers": {
        "last1hour": None,
        "last24hours": None,
        "last5minutes": None
    },
    "nextcloud": {
        "shares": {
            "num_fed_shares_received": None,
            "num_fed_shares_sent": None,
            "num_shares": None,
            "num_shares_groups": None,
            "num_shares_link": None,
            "num_shares_link_no_password": None,
            "num_shares_mail": None,
            "num_shares_room": None,
            "num_shares_user": None
        },
        "storage": {
            "num_files": None,
            "num_storages": None,
            "num_storages_home": None,
            "num_storages_local": None,
            "num_storages_other": None,
            "num_users": None
        },
        "system": {
            "apps": {
                "app_updates": None,
                "num_installed": None,
                "num_updates_available": None
            },
            "cpuload": None,
            "debug": None,
            "enable_avatars": None,
            "enable_previews": None,
            "filelocking.enabled": None,
            "freespace": None,
            "mem_free": None,
            "mem_total": None,
            "memcache.distributed": None,
            "memcache.local": None,
            "memcache.locking": None,
            "swap_free": None,
            "swap_total": None,
            "theme": None,
            "version": None
        }
    },
    "server": {
        "database": {
            "size": None,
            "type": None,
            "version": None
        },
        "php": {
            "max_execution_time": None,
            "memory_limit": None,
            "upload_max_filesize": None,
            "version": None
        },
        "webserver": None
    }
}
)
def main():
    text = prompt("press(TAB) and (SPACE) to chose: nextPy ", completer=completer)
    os.system("python3 stats-nextcloud.py "+text)


if __name__ == "__main__":
    main()
