import numpy as np,string

def gen_tickets(ticket_num,ticket_len):
    idx = np.random.randint(0,25,ticket_num * ticket_len)
    letters = np.array(list(string.ascii_uppercase))
    s = letters[idx].tostring()
    return [s[i*ticket_len : (i+1)*ticket_len] for i in range(ticket_num)]

print gen_tickets(5,10)