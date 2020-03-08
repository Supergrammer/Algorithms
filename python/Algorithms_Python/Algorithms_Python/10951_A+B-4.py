while(1):
    try: A, B = map(int, input().split())
    except EOFError: break
    print(A + B)