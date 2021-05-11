# #!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# <HTTPretty - HTTP client mock for Python>
# Copyright (C) <2011-2020> Gabriel Falcão <gabriel@nacaolivre.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
from __future__ import unicode_literals


class HTTPrettyError(Exception):
    pass


class UnmockedError(HTTPrettyError):
    def __init__(self, message='Failed to handle network request', request=None, address=None):
        hint = 'hint: set httpretty.allow_net_connect = True to allow unknown requests through a real TCP connection.'
        if request:
            headers = dict(request.headers)
            message = 'Intercepted unregistered request {request.method} {request.url} with headers {headers}: {message}'.format(**locals())

        if isinstance(address, (tuple, list)):
            address = ":".join(map(str, address))

        if address:
            hint = 'address: {address} | {hint}'.format(**locals())

        self.request = request
        super(UnmockedError, self).__init__('{message} ({hint})'.format(**locals()))
