###
# Copyright (c) 2011, Ryan Pendergast
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.conf as conf
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import pingdom
import time

class Pingdom(callbacks.Plugin):
    """Add the help for "@plugin help Pingdom" here
    This should describe *how* to use this plugin."""
    threaded = True
    
    def __init__(self, irc):
        self.__parent = super(Pingdom, self)
        self.__parent.__init__(irc)
        self.pingdom_api_key = self.registryValue('pingdomApiKey')
        self.username = self.registryValue('pingdomUser')
        self.pw = self.registryValue('pingdomPW')

    def getcheck(self, irc, msg, args, checkname):
        """[<check name>]
    
        Get the status of a check by name. Default is to return all checks.
        """
        c = pingdom.PingdomConnection(self.username, self.pw, self.pingdom_api_key)

        if checkname:
            checks = c.get_all_checks([checkname])
        else:
            checks = c.get_all_checks()    
                
        for check in checks:
            replyStr = str(check.name) + " | status: " + str(check.status) + " | last response: " + str(check.lastresponsetime)
            if hasattr(check, 'lasterrortime'):
                replyStr = replyStr + " | last error: " + str(time.strftime("%x %X %Z", time.gmtime(check.lasterrortime)))
            else:
                replyStr = replyStr + " | last error: NONE"
                    
            irc.queueMsg(ircmsgs.privmsg(msg.nick, replyStr))
            
    getcheck = wrap(getcheck,[optional('anything')])#   
    
Class = Pingdom


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
