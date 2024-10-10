def unxor_string(data):
  #function to unxor the string, the data part of the algorithm can be replaced depending on your strings needs.
    res = []
    data = data.encode('utf-8').decode('unicode_escape').encode('latin1') #I couldn't find any way of getting the whole value from the binary ninja API, so this converts the escaped string Binja returns. 
    for i in range(len(data)):
        res.append( ((data[i]) ^ ((i % 0x39) + 0x34)))
    chars = []    
    for i in res:
        chars.append(chr(i))
    restring = ''.join(chars)
    return restring

mlil_instrs = bv.get_functions_by_name("functionnamegoeshere")[0].mlil #Get the MLIL for the function you wish to parse through. Alternatively you could do the entire program. 

memcpy = 0x140236790 
strncpy = 0x1402367a8
strcpy = 0x1402367a0
for inst in mlil_instrs.instructions:
    if inst.operation == MediumLevelILOperation.MLIL_CALL:
        if (inst.dest.value == memcpy) or (inst.dest.value == strncpy) or (inst.dest.value == 0x1402367a0):
            if len(inst.params) > 1:
                print("%s: %s" %(inst.params[0], unxor_string(str(inst.params[1]).replace('"', '')))) "print every output"
        
