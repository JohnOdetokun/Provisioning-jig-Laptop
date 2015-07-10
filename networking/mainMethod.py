import pexpect


class openUpdate:
    
    def __init__(self):
        
        self.firm_Upgrade = pexpect.spawn("java com.st.stlinkupgrade.app.MainApp")
        state = self.firm_Upgrade.expect("")
        
    def __enter__(self):
        return self
    
    def __exit__(self):
        self.firm_Upgrade.terminat(False)
        
        
        