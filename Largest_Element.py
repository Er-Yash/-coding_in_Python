def largest( arr, n):
    M=float('-inf')
    for i in range(n):
        if M<arr[i]:
            M=arr[i]
    return M
