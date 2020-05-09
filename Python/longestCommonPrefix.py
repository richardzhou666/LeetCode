def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if '' in strs:
        return ''
    strs.sort(key=len)
    n = len(strs[0])  # smallest length of string
    for i in range(1, n + 1):
        result = [element[:i] for element in strs]
        if all(element == result[0] for element in result) != True:
            if result[0][:i - 1] == '':
                return ""
            return result[0][:i - 1]
            break
    return result[0][:i]
