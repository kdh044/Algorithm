def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(3, total + 1):
        if total % height == 0:
            width = total // height
            
            if width >= height and (width - 2) * (height - 2) == yellow:
                return [width, height]