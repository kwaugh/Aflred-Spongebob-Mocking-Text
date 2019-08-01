import sys
from workflow import Workflow

def main(wf):
    text = wf.args[0]

    if not text:
        wf.send_feedback()

    mock_text = "".join([c.lower() if i % 2 == 0 else c.upper() for i,c in
        enumerate(text)])

    wf.add_item(
        title=mock_text, subtitle='Press enter to copy to clipboard',
        arg=mock_text, valid=True)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
