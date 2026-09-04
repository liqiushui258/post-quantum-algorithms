from kyber_py.ml_kem import ML_KEM_768

ek, dk = ML_KEM_768.keygen()

print("Alice's public key", len(ek), "bytes")
print("Alice's private key:", len(dk), "bytes")


shared_secret_bob, ciphertext = ML_KEM_768.encaps(ek)

print("Ciphertext:", len(ciphertext), "bytes")
print("Bob's shared secret:", shared_secret_bob.hex())

shared_secret_alice = ML_KEM_768.decaps(dk, ciphertext)

print("Alice's shared secret:", shared_secret_alice.hex())

if shared_secret_alice == shared_secret_bob:
    print("ML-KEM shared secret successfully established!")
else:
    print("Something went wrong!")