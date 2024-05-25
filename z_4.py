def sr_arifm(*args):
    summa = sum(args)
    count = len(args)
    if count == 0:
        return None
    else:
        return summa/count

if __name__ == '__main__':
    print(sr_arifm(5,35,25,15))
    print(sr_arifm())