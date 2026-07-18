import ecdsa
from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# ✅ Konwersja danych do liczb całkowitych
r1 = int("845ec6e7e1b1c34e38641e7e8365be07a6af72984270758a6a68768ca39f3099", 16)
s1 = int("2e9cf801cd21dff723133c374f543fda1afab4582060d9d4c33c052a1dc79736", 16)
z1 = int("27b8d1171f9d5508f903329e7a35b0485f6018b807da5d4a645fcb8eae039740", 16)

r2 = int("8494ab073c3029cc964f9180c3f59115eb9c7e0536174b8dc79f4c5cb65df64b", 16)
s2 = int("718aed1d33ad2c892b76d4b0da3bc15db9765a9093cf58ed8bb285ed3dcf9f", 16)
z2 = int("a60da52b429112ae4cec8129a1445155ef2bdf7b711943452b51cc9ef130af8c", 16)

# ✅ Stała wartość krzywej secp256k1 (order n)
n = generator_secp256k1.order()

# ✅ Obliczenie `k`
delta_s = (s1 - s2) % n
delta_z = (z1 - z2) % n

if delta_s != 0:
    k = (delta_z * inverse_mod(delta_s, n)) % n
    print(f"\n✅ Wykryto liniową zależność k! k = {hex(k)}")
else:
    print("\n❌ Brak liniowej zależności w k")
    exit()

# ✅ Obliczenie `d`
d1 = ((s1 * k - z1) * inverse_mod(r1, n)) % n
d2 = ((s2 * k - z2) * inverse_mod(r2, n)) % n

if d1 == d2:
    print(f"\n✅ 🔥 Obliczony klucz prywatny d = {hex(d1)}")
else:
    print("\n❌ Coś jest nie tak - d1 ≠ d2! Możliwe, że to błąd w danych.")

