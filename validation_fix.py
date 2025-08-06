'''modify validation file

1 functiom:
    - fix
'''

def fix(inp: str, out: str) -> None:
    '''fix spaces in validation file

    Parameters:
        inp: filename for modify
        out: filename to write

    Returns:
        None
    '''
    fh = open(inp)
    fw = open(out, 'w')
    for line in fh:
        fw.write(line.replace("  ", ''))
    fh.close()
    fw.close()