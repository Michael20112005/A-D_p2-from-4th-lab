def rabin_karp_search(haystack, needle):
    result = []
    if not haystack or not needle:
        return result

    haystack_len = len(haystack)
    needle_len = len(needle)
    base = 26
    modulus = 10 ** 9 + 7

    needle_hash = 0
    window_hash = 0
    for i in range(needle_len):
        needle_hash = (needle_hash * base + ord(needle[i])) % modulus
        window_hash = (window_hash * base + ord(haystack[i])) % modulus

    base_l_minus_1 = pow(base, needle_len - 1, modulus)

    for i in range(haystack_len - needle_len + 1):
        if window_hash == needle_hash:
            if haystack[i:i + needle_len] == needle:
                result.append(i)
        if i < haystack_len - needle_len:
            window_hash = (window_hash - ord(haystack[i]) * base_l_minus_1) % modulus
            window_hash = (window_hash * base + ord(haystack[i + needle_len])) % modulus
            window_hash = (window_hash + modulus) % modulus

    return result
