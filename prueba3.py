import pyperclip
pyperclip.waitForPaste()  # Doesn't return until non-empty text is on the clipboard.
pyperclip.copy('original text')
pyperclip.waitForNewPaste()  # Doesn't return until the clipboard has something other than "original text".