def doanhthu(n):
    return n  # assuming 'n' is the revenue

def chiphi(n):
    return n  # assuming 'n' is the cost

def roi(doanhthu, chiphi):
    roi = (doanhthu - chiphi) / chiphi
    return roi

doanhthu_value = doanhthu(100)
chiphi_value = chiphi(10)
roi_value = roi(doanhthu_value, chiphi_value)

print("ROI: ", roi_value)
if roi_value >= 0.75:
    print("Bạn nên đầu tư")
else:
    print("Bạn không nên đầu tư")
