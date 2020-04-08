from base64tool import Base64Tool
from returncode import Returncode
import sys
import os
import traceback
import logging
from utils.logger import Logger

class ProjectCore :

     return_code = None

     def __init__(self, debug_level=logging.DEBUG) :
         self.logger = Logger(debug_level).logger

         try :
             self.return_code = Returncode()
         except :
             exit()
