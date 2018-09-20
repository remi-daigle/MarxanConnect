
import marxanconpy.marcon
import marxanconpy.metrics
import marxanconpy.manipulation
import marxanconpy.posthoc
import marxanconpy.spatial

import wx

MarxanConnectVersion = "v0.1.2"

def progress_bar_update(count, dlg, keepGoing, n, progressbar=True):
    count += n
    (keepGoing, skip) = dlg.Update(count)

def warn_dialog(self, message, caption="Warning!"):
    """
    Warning
    """
    wx.MessageBox(message, caption, style=wx.OK | wx.ICON_WARNING)