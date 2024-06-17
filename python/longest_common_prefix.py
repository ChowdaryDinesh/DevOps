def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
    
# Example usage
strs = ["flower", "flow", "flight"]
print(f"Longest common prefix: {longest_common_prefix(strs)}")  # Output: "fl"
