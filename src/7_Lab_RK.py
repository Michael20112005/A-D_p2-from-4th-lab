def rabin_karp_search(haystack, needle, base=26, divisor=1001):
    result = []
    if not haystack or not needle:
        return result

    haystack_len = len(haystack)
    needle_len = len(needle)

    needle_hash = 0
    window_hash = 0
    for i in range(needle_len):
        needle_hash = (needle_hash * base + ord(needle[i])) % divisor
        window_hash = (window_hash * base + ord(haystack[i])) % divisor

    base_l_minus_1 = pow(base, needle_len - 1, divisor)

    for i in range(haystack_len - needle_len + 1):
        if window_hash == needle_hash:
            if haystack[i:i + needle_len] == needle:
                result.append(i)
        if i < haystack_len - needle_len:
            window_hash = (window_hash - ord(haystack[i]) * base_l_minus_1) % divisor
            window_hash = (window_hash * base + ord(haystack[i + needle_len])) % divisor
            window_hash = (window_hash + divisor) % divisor

    return result
