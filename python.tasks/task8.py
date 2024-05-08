speed=int(input("Enter Speed"))
good_speed=70
if speed<=70:
    print("ok")
elif speed>70:
    overspeed=speed-good_speed
    Demerit_points=overspeed/5
    print("Demerit Points=",Demerit_points)
    if Demerit_points>12:
        print("License Suspended")




