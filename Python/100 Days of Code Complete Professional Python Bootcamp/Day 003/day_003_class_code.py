# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:19:05 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

# Day: 003
# Conditional Statements, Logical Operators, Code Blocks and Scope

# Conditional IF/ELSE

'''
if condition:
    do this
else:
    do this
'''

water_level = 50

if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

# Link to Flow chart 1 : https://www.draw.io/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%201#R1VfbcpswEP0apk%2FJAAJfHmM7aR%2FSjlt3ps2jYm1ArUCukC%2Fk67sywqDgJM7Eub0w6Ggl7Z49uwKPjLPNZ0UX6VfJQHihzzYemXhhOIhCfBqgrICIkApIFGcVFDTAjN%2BCBX2LLjmDwjHUUgrNFy44l3kOc%2B1gVCm5ds1upHBPXdAEOsBsTkUX%2FcWZTm1YYb%2FBvwBP0vrkoDesZjJaG9tIipQyuW5B5NwjYyWlrt6yzRiE4a7mpVp3cc%2FszjEFuT5kwTQf3Pz8rmYwjVc%2FVmxzyf%2FJExtGocs6YGAYvx1KpVOZyJyK8wYdKbnMGZhdfRw1NpdSLhAMEPwDWpc2mXSpJUKpzoSdRYdV%2BdusP%2B2RsAauEDjxT%2F1%2BXCOTjT2jGpXt0RQUz0CDsmAVh3H%2BXnosVMilmsMDnNQyoyoB%2FYBdvEsiih8keqNKXKdAUM1Xrh%2FUyjDZ2dmlZ0rRsmWwkDzXRWvnqQHQwBYUIbagbD0FcdzOOr5UO9ajlmsNtFXGE1QyfGOVREHUVon%2FQQQSHUMgHQUEkSuAoe%2FuULllFzXKeKrQer3X15nlYkXF0rJje6tpbT2aoXBGid4m0w%2Bw52ceuehIU6Uyu15ilKN1yjXMFnSbzDVeT67A7GGgNGwe1kQ3h%2FWCoO%2ByVF9b6%2BauCHoWS1v3xN2ktdPe4vjpFJK3KNUj1lZ4YG3dk5eDa%2BtZJIcdnc7QYd2V4o7Y4HE53nAhxlJItV1LWAwDZtpeoZX8C62ZQXhNsDqPI2DiCjjco99wj36jl9Jv1KF2TPNPpgPg5yE8j%2BEj8EV8l6499T7ovyJd8T663gtZYb%2F%2Fvtiqz2%2FR9U12aMKAtcsFFTzJ8X2OgZsPipGhheNPwpmdyDhjVSuFgt%2FS6%2B1WppnaWxb3jUdePDF7YfcsqkZ6JJoHd%2B4gMuywTPaUcPhiLHev8SsoPjzN%2BC%2F7KM%2FRcXjGYfNfWH1cNT%2FX5Pw%2F

# Comparison Operators
# >, <, <=, >=, ==, !=

# Nested IF/ELSE

'''
if condition:
    do this
    if another conditon:
        do this 
    else:
        do this
else:
    do this
'''

# Link to Flow Chart 2 : https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload

# Link to FLow Chart 3 : https://www.draw.io/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload

# Mutliple IF conditions

'''
if condition A:
    do this
if condition B:
    do this
if condition c:
    do this
else:
    do this
'''

# Link to Flow Chart: https://www.draw.io/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload

# Logical Operators

'''
A and B
A or B
not A
'''

# Link to Flow Chart : https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day%203%20Logical%20Operators.drawio#R7VtZc9o6FP41zH2iY0teH0uWZpqkQy%2BZ29CXOwYrthNjUVkQyK%2BvjGWwLbEFL6HTzCSxjyVhfec7myQ68GKy%2BEKcqX%2BPXRR2gOIuOvCyA4CqAYP9SyTLVGJqXOCRwOWNNoJB8Ia4UOHSWeCiuNCQYhzSYFoUjnEUoTEtyBxC8Gux2RMOi586dTwkCAZjJxSlPwKX%2BqnUAuZGfoMCz88%2BWTXs9MnEyRrzmcS%2B4%2BLXnAhedeAFwZimV5PFBQoT8DJc0n7XW56uX4ygiB7SoR9ZTw%2FfyQD19fm%2Fc3dxF%2FzCXT6NmC6zCSOXzZ%2FfYkJ97OHICa820h7Bs8hFyagKu9u0ucN4yoQqEz4jSpdcmc6MYiby6STkT9kLk%2BVj0v%2BTAUEmGDJBV%2FmkmHomuVzwz0jvlvm7PiLBBFFEuFBEgwMU4xkZox0QZKxyiIfojnZ62i7BJ%2FcBHOsvCLO3IUvWgKDQocG8yB%2BH09Bbt%2BNdPxPiLHMNpjiIaJwbuZ8IWANuUZABthqR25Oq63mts4t0xOwu92ob0YoZR7DEbpklmqrlWaJ8TIJotRBEYICqFQlgK8UR0vfknTbMOJZohtE8zzgWcyeccXS4b01cm%2BFMGHF6Hl0pU1GZz5904LVATeLjyWjGZtl79QOKBlNnpd1XFp%2BKBNvKiDkiFC126jB7qppFlLKw9bqJFarBZX4uTpSVlld7DuPjIYRtmOr7bQscaFtq1bZ1EshA4OmAzYCKVFwDq%2B6n41MQhhc4xGTVF7o6stzE7cWU4BeUe2KBEWTWWQ2BYZHAQMJfIOGvVhd%2FNQHaCyf6J%2FEALD1EpyFcAV5QKcIlsXfLrAeuy682%2BL%2F%2FzaXPLvk%2BvOl71zdexsRzMXddNHfptD6WuesyTn4URgKzZMENUlLuqhUBrm9YgInNjhaxcMLAi9j1mGGRZG29BIOAVWKf%2BYNJ4LopgVEcvDmj1VAJhXkqw8bVex39MhmLcTZO6VsRzFYp0ENbQBlK%2FCSoDWUxVxqi%2BOxhBpa2F2etJpylnkiMR2143FwttK6OD6mEDvLUuzzwXk9tVO2p5dUIUJKZ55kBgV4cZEvd847aRA6I8lfx%2BXZWWyFa%2FtZ%2FzbLQzm4tgVKGP3%2B8PfT6PwfImj8%2BPAS9STtZKloE9DF3Pdzoid1tNJPcFFaO2laoFMLWMuJdb52LiskyepsrMcASAoQiSYQlqYNeW23Wsk9qhsD1JADHrlaqsKh8zSpthpTzCRvual9c3tzbWy8XUzXnIoYkKWUq1HTRBBuuRu3i%2Bgi0RBu0a1pOkiJlCkjdoThOHK6%2FKuElecO5lUxqGfMD%2FV5tJRNoJVN%2BvwerPJPdsnMHyhFKL6ugZrdhbXEb4iZw84tYejl6t%2B051vRpJ3qrzUTvyuuEd0VvXTkuekPNOiF6l3s3Hb3tLWYoiUVN26FmfLD4LVnmVEFXtc4%2BakNV8Hi6iLXeZNxWoYg1A1rBJPnDpnb%2BoB%2BQKpmNpkqyTH6rD1D2%2BwBhs9gYW2j0VNpejnCUqMB1Yn%2FtXCqAVzeL8AKJ91Bl%2BK6PSJwCsH3%2F%2BGI8erfgFvwKlvfPN8v%2BfVekdBtR%2FaD4vGvZJ7885M%2FnXfx0iYKv9n%2Bz5a06uDNesnnWncPqalHDh2awRx8%2BsuSZcmWnj3ZgLcRlsZxpOiwbWnthWQqVaFafPYYHUJIlCKXLfnVxLeLcooVuvm9BsYpoITXyViqSg3zXLp%2B013dVfrD2JJBbCRDZXkW2IXHkXgWofrPiJI2aH0qjorN6dSJ%2BpjRMPNKIZbbG6lzp1MfMi5x0qlTIwJTVjzwDq8BLlQ%2FqrkNyPulSbNFNWXW5Ka1VC1pbzTD3pIXdvl2u7swMSDz%2FliZG4lnjoxKjpi0FlnZtDNlhbaWmNEoKrFj9%2FQlnuMo4r9fXGjjDtcuacjA%2F%2BCgxQ0ydpPMoSMeIVzFBW5wXrVmeWoDblKSpKrCz1aZGiC3uNPwBR0ABLEVaCa8rOgPKbjdfDEzr283XK%2BHVbw%3D%3D
