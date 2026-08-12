import hmac
import hashlib

def secure_hash(integrity_salt, payload_data):

    valid_keys = []
    for key in payload_data:
        if key.startswith('pp_') and key != 'pp_SecureHash':
            valid_keys.append(key)

    valid_keys.sort()

    values_list = []
    for key in valid_keys:
        value = str(payload_data[key])
        if value != '':
            values_list.append(value)

    hash_string = integrity_salt + '&' + '&'.join(values_list)

    return hmac.new(
        integrity_salt.encode('utf-8'),
        hash_string.encode('utf-8'),
        hashlib.sha256
    
    ).hexdigest().upper()