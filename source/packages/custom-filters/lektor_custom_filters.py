# -*- coding: utf-8 -*-
# Third-party
from dateutil import parser
from lektor.pluginsystem import Plugin


class CustomFiltersPlugin(Plugin):
    name = "custom-filters"
    description = u"custom Jinja2 filters"

    def on_setup_env(self, **extra):
        def parsedatetime_filter(value):
            datetime_obj = parser.parse(value)
            return datetime_obj

        self.env.jinja_env.filters["parsedatetime"] = parsedatetime_filter
