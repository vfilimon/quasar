#!/usr/bin/env python
# encoding: utf-8
'''
configurationGenerators.py

@author:     Damian Abalo Miron <damian.abalo@cern.ch>
@author:     Piotr Nikiel <piotr@nikiel.info>

@copyright:  2015 CERN

@license:
Copyright (c) 2015, CERN, Universidad de Oviedo.
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

@contact:    damian.abalo@cern.ch
'''

import os
import subprocess
import platform
import shutil
from transformDesign import transformDesignVerbose

configPath = "Configuration" + os.path.sep	
def generateConfiguration():
	"""Generates the file Configuration.xsd. This method is called automatically by cmake, it does not need to be called by the user."""
	output = "Configuration.xsd"
	returnCode = transformDesignVerbose(configPath + "designToConfigurationXSD.xslt", configPath + output, 0, 0)
	print("Calling xmllint to modify " + output)
	returnCode = subprocess.call("xmllint --xinclude " + configPath + output + " > " + configPath + output + ".new", shell=True)
	if returnCode != 0:
		print("ERROR: There was an problem executing xmllint")
		return returnCode
	else:
		print("Coping the modified file  " + output + ".new into the name of " + output)
		shutil.copyfile(configPath + output + ".new", configPath + output)
		return 0
	print("ERROR: Unknown platform")
	return -1

def generateConfigurator():
	"""Generates the file Configurator.cpp. This method is called automatically by cmake, it does not need to be called by the user."""
	output = "Configurator.cpp"
	returnCode = transformDesignVerbose(configPath + "designToConfigurator.xslt", configPath + output, 0, 1)
	return 0
	
def generateConfigValidator():
	"""Generates the file ConfigValidator.xsd. This method is called automatically by cmake, it does not need to be called by the user."""
	output = "ConfigValidator.cpp"
	returnCode = transformDesignVerbose(configPath + "designToConfigValidator.xslt", configPath + output, 0, 1)
	return 0
			