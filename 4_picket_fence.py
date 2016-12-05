# Picket Fence Cipher

m = "makeyourmessagesecureabcde" # this can be any string of ASCII characters, of any length
m_no = 0
k = 4 # in this case, this is the number of rows in the rail
order = []
c = []
re_order = []
m_proof = []


# create "order" list
repetitions = int((len(m) / k)) + 1

for i in range(0,k):
    for j in range(0,repetitions):
        index = (i + (j * k))
        if index > len(m) - 1:
            continue
        else:
            order.append(index)

print(order)

# encryption function

c = [m[i] for i in order]
print(c)

# create "reorder" list ## this isn't correct yet

m_no = (len(c) / k) + 1
repetitions = int((len(c) / k)) + 1

for i in range(0,repetitions):
    for j in range(0,k+1):
        index = (i + (j * repetitions))
        if index > len(m) - 1:
            continue
        else:
            re_order.append(index)
print(re_order)

m_proof = [c[i] for i in re_order[0:len(m)]]
m_proof = ''.join(m_proof)
print(m_proof)

if m_proof == m:
    print("Heck yeah, proofed")
else:
    print("Fail Whale")
