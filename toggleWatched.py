import xbmc

file = xbmc.getInfoLabel("ListItem.FilenameAndPath")

xbmc.executebuiltin("Action(ToggleWatched)")
