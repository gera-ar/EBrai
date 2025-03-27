# -*- coding: utf-8 -*-
# Copyright (C) 2025 Gerardo Kessler <ReaperYOtrasYerbas@gmail.com>
# This file is covered by the GNU General Public License.

import appModuleHandler
from scriptHandler import script
import api
from ui import message

class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		self.status_object= None

	def objSearch(self):
		for obj in api.getForegroundObject().getChild(1).children:
			try:
				if obj.UIAAutomationId == 'EBBarraEstado':
					self.status_object= obj.getChild(4)
			except:
				continue

	@script(gesture="kb:control+shift+c")
	def script_positionAnnounce(self, gesture):
		if not self.status_object: self.objSearch()
		current_line= self.status_object.getChild(7).name.split(',')[0]
		message(current_line)

	@script(gesture="kb:control+shift+e")
	def script_statusAnnounce(self, gesture):
		message(self.status_object.name)
