def compress(text):
    if not text: 
        return ""
    
    result = ""
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + (str(count) if count > 1 else "")
            count = 1
            
    result += text[-1] + (str(count) if count > 1 else "")
    return result

inp=input("Enter alphabets: ")
print(compress(inp))
