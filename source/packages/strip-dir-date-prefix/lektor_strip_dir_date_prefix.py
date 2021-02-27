# -*- coding: utf-8 -*-
# Standard library
import re

# Third-party
from lektor.pluginsystem import Plugin

RE_DATE_PREFIX = re.compile(r"^(\d{8}-)(.*)$")


class StripDirDatePrefixPlugin(Plugin):
    name = "strip-dir-date-prefix"
    description = u"Jinja filter to strip XXXX-XX- date prefix"

    def on_setup_env(self, **extra):
        def stripdateprefix_filter(value):
            matches = RE_DATE_PREFIX.match(value)
            if matches:
                return matches[2]
            else:
                return value

        self.env.jinja_env.filters["stripdateprefix"] = stripdateprefix_filter
