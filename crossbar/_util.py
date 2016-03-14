#####################################################################################
#
#  Copyright (C) Tavendo GmbH
#
#  Unless a separate license agreement exists between you and Tavendo GmbH (e.g. you
#  have purchased a commercial license), the license terms below apply.
#
#  Should you enter into a separate license agreement after having received a copy of
#  this software, then the terms of such license agreement replace the terms below at
#  the time at which such license agreement becomes effective.
#
#  In case a separate license agreement ends, and such agreement ends without being
#  replaced by another separate license agreement, the license terms below apply
#  from the time at which said agreement ends.
#
#  LICENSE TERMS
#
#  This program is free software: you can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License, version 3, as published by the
#  Free Software Foundation. This program is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU Affero General Public License Version 3 for more details.
#
#  You should have received a copy of the GNU Affero General Public license along
#  with this program. If not, see <http://www.gnu.org/licenses/agpl-3.0.en.html>.
#
#####################################################################################

import inspect


def class_name(obj):
    """
    This returns a name like "module.Class" given either an instance, or a class.
    """

    if inspect.isclass(obj):
        cls = obj
    else:
        cls = obj.__class__
    return '{}.{}'.format(cls.__module__, cls.__name__)


class WampPrefixCaller(object):
    def __init__(self, session, prefix):
        self._session = session
        self._prefix = prefix

    # or could override __getattribute__ etc returning objects that
    # implement __call__ and provide "magic" access, like
    # caller.foo("arg")
    def call(self, method, *args, **kw):
        return self._session.call(method, *args, **kw)
