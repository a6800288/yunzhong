#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0muMDAU Server
from core import app 
import os, logging
from conf import setting
from core.index import main
from core.user import auth , register 
# muMDAU_app setting
app.secret_key = setting.yourkey
app.register_blueprint(main)
app.register_blueprint(auth, url_prefix="/login")
app.register_blueprint(register, url_prefix="/register")
# Main function of MDAUServer
if __name__ == '__main__':
    # log writeing
    print('Yakumo is run on ' + str(setting.host) + ':' + str(setting.port))
    # check debug
    if setting.debug == 0:
        debugB = False 
        app.run(debug=debugB, host=str(setting.host), port=setting.port)
    else:
        debugB = True
        logging.basicConfig(filename=setting.s_log, level=logging.WARNING)
        logdebug = open(setting.s_log, 'w')
        print('!!!Important : Now is in debug mode.')
        app.run(debug=debugB, host=str(setting.host), port=setting.port)
