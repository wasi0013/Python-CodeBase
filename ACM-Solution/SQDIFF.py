import math

r =3 
R =4
d =3**0.5
part1 = r*r*math.acos((d*d + r*r - R*R)/(2*d*r));
part2 = R*R*math.acos((d*d + R*R - r*r)/(2*d*R));
part3 = 0.5*math.sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R));

intersectionArea = part1 + part2 - part3;
print(intersectionArea)
