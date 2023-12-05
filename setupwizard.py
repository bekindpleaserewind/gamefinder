import os
import yaml

from PySide6.QtWidgets import QWizard, QWizardPage

from appinfo import Info
from path import Pathinfo
from wizardpage1 import Ui_WizardPage1
from wizardpage2 import Ui_WizardPage2

class SetupWizardPage2Data:
     appid = None
     certid = None
     devid = None
     token = None

class SetupWizardPage1(QWizardPage, Ui_WizardPage1):
    def __init__(self):
        super(SetupWizardPage1, self).__init__()
        self.setupUi(self)
        self.pathinfo = Pathinfo()

class SetupWizardPage2(QWizardPage, Ui_WizardPage2):
    def __init__(self):
        super(SetupWizardPage2, self).__init__()
        self.setupUi(self)
        self.registerField('production_appid*', self.lineEditAppid)
        self.registerField('production_certid*', self.lineEditCertid)
        self.registerField('production_devid*', self.lineEditDevid)
        self.registerField('production_token*', self.lineEditToken)

    def initializePage(self):
        if os.path.exists(self.pathinfo.ebay):
            with open(self.pathinfo.ebay, "r") as fd:
                config = yaml.load(fd, Loader=yaml.SafeLoader)
                self.lineEditAppid.setText(config['api.ebay.com']['appid'])
                self.lineEditCertid.setText(config['api.ebay.com']['certid'])
                self.lineEditDevid.setText(config['api.ebay.com']['devid'])
                self.lineEditToken.setText(config['api.ebay.com']['token'])
                self.completeChanged.emit()

    def isComplete(self):
        if len(self.lineEditAppid.text()) > 0 and len(self.lineEditCertid.text()) > 0 and len(self.lineEditDevid.text()) > 0 and len(self.lineEditToken.text()) > 0:
            return True
        return False

class SetupWizard(QWizard):
    def __init__(self, parent=None, stopConnection = False):
        self.window = parent
        self.stopConnection = stopConnection
        super(SetupWizard, self).__init__(parent)

        self.pathinfo = Pathinfo()

        self.dataPage2 = SetupWizardPage2Data()

        page1 = SetupWizardPage1()
        self.addPage(page1)

        page2 = SetupWizardPage2()
        self.addPage(page2)

    def accept(self):
        self.dataPage2.appid = self.field('production_appid')
        self.dataPage2.certid = self.field('production_certid')
        self.dataPage2.devid = self.field('production_devid')
        self.dataPage2.token = self.field('production_token')

        if self.generateEbayYaml():
            if self.window is not None:
                if os.path.exists(self.pathinfo.ebay):
                    self.window.button_start.setDisabled(False)
                else:
                    self.window.button_start.setDisabled(True)

                self.window.show()
                self.hide()

                return True

        if os.path.exists(self.pathinfo.ebay):
            self.window.button_start.setDisabled(False)
        else:
            self.window.button_start.setDisabled(True)

        return False

    def generateEbayYaml(self):
        ebayYaml = {
            'name': 'ebay_api_config',
            'api.sandbox.ebay.com': {
                'compatability': '719',
                'appid': '',
                'certid': '',
                'devid': '',
                'token': '',
             },
             'api.ebay.com': {
                'compatability': '719',
                'appid': self.dataPage2.appid,
                'certid': self.dataPage2.certid,
                'devid': self.dataPage2.devid,
                'token': self.dataPage2.token,
             },
             'svcs.ebay.com': {
                  'appid': self.dataPage2.appid,
             },
             'open.api.ebay.com': {
                  'appid': self.dataPage2.appid,
             },
        }

        # stop connection
        if self.stopConnection and os.path.exists(self.pathinfo.ebay):
            self.window.stop()

        ebayYamlPath = self.pathinfo.ebay
        try:
            with open(ebayYamlPath, 'w') as fd:
                yaml.dump(ebayYaml, fd)
        except:
            return False

        return True
