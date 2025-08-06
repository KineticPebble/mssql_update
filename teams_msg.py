'''Teams- channel connection handling

2 function:
    - log_html
    - msg_teams
'''
import pymsteams
import auth

myTeamsMessage = pymsteams.connectorcard(auth.hook)

def log_html(log: str) -> str:
    '''conevert log into html

    Parameters:
        log: log file fullpath

    Returns:
        html
    '''
    fh = open(log)
    html = ''
    for line in fh:
        html += f"{line.strip()}<br/>"
    return html

def msg_teams(content: str, subject: str) -> None:
    '''send message

    Parameters:
        content: the message body
        subject: message heading

    Returns:
        None
    '''
    myTeamsMessage.text(subject+":<br/>"+content)
    myTeamsMessage.send()



