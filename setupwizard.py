import os
import yaml

from PySide6.QtWidgets import QWizard, QWizardPage

from appinfo import Info
from wizardpage1 import Ui_WizardPage1
from wizardpage2 import Ui_WizardPage2
from wizardpage3 import Ui_WizardPage3

class SetupWizardPage2Data:
     appid = None
     certid = None
     devid = None
     token = None

class SetupWizardPage3Data:
     appid = None
     certid = None
     devid = None
     token = None

class SetupWizardPage1(QWizardPage, Ui_WizardPage1):
    def __init__(self):
        super(SetupWizardPage1, self).__init__()
        self.setupUi(self)

class SetupWizardPage2(QWizardPage, Ui_WizardPage2):
    def __init__(self, parent = None):
        super(SetupWizardPage2, self).__init__(parent)
        self.setupUi(self)
        self.registered = False

    def initializePage(self):
        if os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')):
            with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml'), "r") as fd:
                config = yaml.load(fd, Loader=yaml.SafeLoader)
                self.lineEditAppid.setText(config['api.sandbox.ebay.com']['appid'])
                self.lineEditCertid.setText(config['api.sandbox.ebay.com']['certid'])
                self.lineEditDevid.setText(config['api.sandbox.ebay.com']['devid'])
                self.lineEditToken.setText(config['api.sandbox.ebay.com']['token'])

        if not self.registered:
            self.registerField('sandbox_appid*', self.lineEditAppid)
            self.registerField('sandbox_certid*', self.lineEditCertid)
            self.registerField('sandbox_devid*', self.lineEditDevid)
            self.registerField('sandbox_token*', self.lineEditToken)
            self.registered = True
        
    #def isComplete(self):
    #    if os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')):
    #        if len(self.lineEditAppid.text()) > 0 and len(self.lineEditCertid.text()) > 0 and len(self.lineEditDevid.text()) > 0 and len(self.lineEditToken.text()) > 0:
    #            return True
    #    super(SetupWizardPage2, self).isComplete() 

class SetupWizardPage3(QWizardPage, Ui_WizardPage3):
    def __init__(self):
        super(SetupWizardPage3, self).__init__()
        self.setupUi(self)
        self.registered = False

    def initializePage(self):
        if os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')):
            with open(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml'), "r") as fd:
                config = yaml.load(fd, Loader=yaml.SafeLoader)
                self.lineEditAppid.setText(config['api.ebay.com']['appid'])
                self.lineEditCertid.setText(config['api.ebay.com']['certid'])
                self.lineEditDevid.setText(config['api.ebay.com']['devid'])
                self.lineEditToken.setText(config['api.ebay.com']['token'])
        if not self.registered:
            self.registerField('production_appid*', self.lineEditAppid)
            self.registerField('production_certid*', self.lineEditCertid)
            self.registerField('production_devid*', self.lineEditDevid)
            self.registerField('production_token*', self.lineEditToken)
            self.registered = True

        #self.setField('production_appid', self.lineEditAppid)
        #self.setField('production_certid', self.lineEditCertid)
        #self.setField('production_devid', self.lineEditDevid)
        #self.setField('production_token', self.lineEditToken)

    #def isComplete(self):
    #    if os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')):
    #        if len(self.lineEditAppid.text()) > 0 and len(self.lineEditCertid.text()) > 0 and len(self.lineEditDevid.text()) > 0 and len(self.lineEditToken.text()) > 0:
    #            return True
    #    super(SetupWizardPage3, self).isComplete() 

class SetupWizard(QWizard):
    def __init__(self, parent=None, restartConnection = False):
        self.window = parent
        self.restartConnection = restartConnection
        super(SetupWizard, self).__init__(parent)

        self.dataPage2 = SetupWizardPage2Data()
        self.dataPage3 = SetupWizardPage3Data()

        page1 = SetupWizardPage1()
        self.addPage(page1)

        page2 = SetupWizardPage2()
        self.addPage(page2)

        page3 = SetupWizardPage3()
        self.addPage(page3)

    def accept(self):
        self.dataPage2.appid = self.field('sandbox_appid')
        self.dataPage2.certid = self.field('sandbox_certid')
        self.dataPage2.devid = self.field('sandbox_devid')
        self.dataPage2.token = self.field('sandbox_token')
        self.dataPage3.appid = self.field('production_appid')
        self.dataPage3.certid = self.field('production_certid')
        self.dataPage3.devid = self.field('production_devid')
        self.dataPage3.token = self.field('production_token')

        if self.generateEbayYaml():
            if self.window is not None:
                self.window.show()
                self.hide()
                return True

        return False

    def generateEbayYaml(self):
        ebayYaml = {
            'name': 'ebay_api_config',
            'api.sandbox.ebay.com': {
                'compatability': '719',
                'appid': self.dataPage2.appid,
                'certid': self.dataPage2.certid,
                'devid': self.dataPage2.devid,
                'token': self.dataPage2.token,
             },
             'api.ebay.com': {
                'compatability': '719',
                'appid': self.dataPage3.appid,
                'certid': self.dataPage3.certid,
                'devid': self.dataPage3.devid,
                'token': self.dataPage3.token,
             },
             'svcs.ebay.com': {
                  'appid': self.dataPage3.appid,
             },
             'open.api.ebay.com': {
                  'appid': self.dataPage3.appid,
             },
        }

        ebayYamlPath = os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')
        try:
            with open(ebayYamlPath, 'w') as fd:
                yaml.dump(ebayYaml, fd)
        except:
            return False

        # Restart connection
        if self.restartConnection and os.path.exists(os.path.join(os.environ['APPDATA'], Info.APPNAME, 'ebay.yaml')):
            self.window.stop()
            self.window.start()

        return True
