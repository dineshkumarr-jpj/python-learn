
import hmac
import hashlib


# Secret key
secret = "my_webhook_secret"

# Original message (payload)
payload = b'{"event": "order.created", "id": 101}'


# STEP 1: Generate signature
def generate_signature(payload, secret):

    signature = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()

    return signature


# STEP 2: Verify signature
def verify_signature(payload, signature, secret):

    new_signature = generate_signature(payload, secret)

    return hmac.compare_digest(new_signature, signature)


# STEP 3: Generate original signature
signature = generate_signature(payload, secret)


# TEST 1: Correct payload and correct secret
result1 = verify_signature(payload, signature, secret)

print("Valid signature:", result1)


# TEST 2: Changed payload, but old signature
changed_payload = b'{"event": "order.created", "id": 999}'

result2 = verify_signature(changed_payload, signature, secret)

print("Tampered payload:", result2)


# TEST 3: Correct payload, but wrong secret
wrong_secret = "wrong_secret"

result3 = verify_signature(payload, signature, wrong_secret)

print("Wrong secret:", result3)
