from dilithium_py.ml_dsa import ML_DSA_65

pk, sk = ML_DSA_65.keygen()

print("public key", len(pk), "bytes")
print("private key:", len(sk), "bytes")


message = b"Post-Quantum Cryptography"

signature = ML_DSA_65.sign(sk, message)

print("Signature:", len(signature), "bytes")

valid = ML_DSA_65.verify(pk, message, signature)

print("Signature valid:", valid)
