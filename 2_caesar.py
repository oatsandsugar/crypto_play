# Caesar cypher

m = "abcderfghijklmnopqrstuvwxyz" # this can be any string of ASCII characters, of any length
k = 14
m_ord = []
c_ord = []
c = ""

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

# define Enc
def enc(z):
  for x in z:
    c_ord.append(x + k)

# Enc(m)
enc(m_ord)

print(c_ord)

## Turn c back into letters
for x in c_ord:
  c += chr(x)

print(c)

## mutate c into numbers
for x in c:
  c_ord_proof.append(ord(x))
print(c_ord_proof)

# define Dec
def dec(z):
  for x in z:
    m_ord_proof.append(x - k)

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
