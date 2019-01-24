def approx_integral(f,lo,hi,num_regions):
    d = float(hi-lo)/num_regions
    total=f(lo)/2
    for i in range(1,num_regions):
        total += f(lo+i*d)
    total += f(hi)/2
    return total*d
