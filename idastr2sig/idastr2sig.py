from idautils import *
from idaapi import *
from idc import *
import base64

# version 0.1

def generateSig(signaturepath):
    sc = Strings()
    datastr = {}
    for i in sc:
        if str(i) in datastr:
            datastr.pop(str(i))
        else:
            datastr[str(i)] = i.ea

    with open(signaturepath,"w") as f:
        funcname = ""
        for i in datastr:
            ixrefs = list(XrefsTo(datastr[i]))
            if len(ixrefs) == 1:
                funcname = GetFunctionName(list(XrefsTo(datastr[i]))[0].frm)
                if funcname != "":
                    f.write(funcname + ":" + base64.b64encode(i) + "\n")
            else:
                continue

def loadSig(signaturepath):
    sigdict = {}
    with open(signaturepath,'r') as f:
        lines = f.readlines()
        for line in lines:
            sigdict[base64.b64decode(line.split(':')[1])] = line.split(":")[0]
    sc = Strings()
    datastr = {}
    for i in sc:
        if str(i) in datastr:
            datastr.pop(str(i)) 
        else:
            datastr[str(i)] = i.ea
    for i in datastr:
        if i in sigdict:
            ixrefs = list(XrefsTo(datastr[i]))
            if len(ixrefs) == 1:
                if(get_func(ixrefs[0].frm)):
                    set_name(get_func(ixrefs[0].frm).startEA, sigdict[i])
