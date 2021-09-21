def decrypt(key, data):
    out = ''
    for d in data:
        for k in key:
            d = chr(ord(d) ^ ord(k))
        out += chr(~ord(d) & 255)
    return out


def decrypt_string(ea):
    key = 'I0L0v3Y0u0V1rUs'
    start_ea = ea
    data = ''
    ## Limit the string to 500 max 
    for limit_count in range(500):
        b =  get_bytes(ea, 1)
        if ord(b) == 0:
            ## End of the string data
            break
        data += b
        ea += 1
    ## Decrypt the string
    out = decrypt(key, data)
    return out



def decrypt_all(ea, ea_end):
    while ea <= ea_end:
        b =  get_bytes(ea, 1)
        if ord(b) == 0:
            ea +=1
            continue
        new_str = decrypt_string(ea)
        if is_ascii(new_str):
            print new_str
            replace_string(ea, new_str)
        ea += len(new_str)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def replace_string(ea, new_str):
    ea_start = ea
    for s in new_str:
        patch_byte(ea, ord(s))
        ea += 1
    create_strlit(ea_start, idc.BADADDR)