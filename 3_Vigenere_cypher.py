# Caesar cypher

m = "makeyourmessagesecureabcde" # this can be any string of ASCII characters, of any length
m_ord = []
m_len = 0
k = "sweet"
k_ord = []
k_len = 0
remainder = 0
multiple = 0
k_ord_long = []
c_ord = []

m_proof = ""
m_ord_proof = []
c_ord_proof = []
c_proof = ""

## mutate m into numbers
print(m)
m = m.upper()

for x in m:
    m_ord.append(ord(x))
print(m_ord)

## mutate k into numbers
print(k)
k = k.upper()

for x in k:
    k_ord.append(ord(x))
print(k_ord)

## loop k to be the same length of m  ##this appears to overcompensate

m_len = len(m)
k_len = len(k)
remainder = m_len % k_len
k_len = k_len - remainder

multiple = m_len / k_len

counter = 0

while counter < multiple:
    counter = counter + 1
    for x in k_ord:
        k_ord_long.append(x)

if remainder < 0:
    counter_2 = 0
    while counter_2 < remainder:
        counter = counter + 1
        for x in k_ord:
            k_ord_long.append(x)

print(k_ord_long)

# define Enc
def enc(z):
    for i,x in enumerate(m_ord):
        c_ord.append(m_ord[i] + k_ord_long[i])

# Enc(m)
enc(m_ord)

print(c_ord)

# define Dec
def dec(z):
    for i,x in enumerate(c_ord):
        m_ord_proof.append(c_ord[i] - k_ord_long[i])  # if these were seperate items, the decrypter would have to transform k to k_ord_long themselves

# Dec(c)
dec(c_ord_proof)

print(m_ord_proof)

## Turn m back into letters
for x in m_ord_proof:
  m_proof += chr(x)

print(m_proof)

if m_proof == m:
    print("Heck yeah, proofed")
else:
    print("Fail Whale")
