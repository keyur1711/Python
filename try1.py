try:
    a= int(input())
    b= int(input())
    if b ==5:
        raise ValueError
finally:
    print("mipm")