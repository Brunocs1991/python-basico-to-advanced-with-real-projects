"""
CONSTANT = "Variables" that will not change
Too many conditions in the same if (bad)
<- Complexity count (bad)
"""

speed = 61  # velocidade atual do carro
car_location = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = speed > RADAR_1
car_happened_radar_1 = car_location >= (LOCAL_1 - RADAR_RANGE) and \
    car_location <= (LOCAL_1 + RADAR_RANGE)
car_fine_radar_1 = car_happened_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if car_happened_radar_1:
    print('Carro passou radar 1')

if car_fine_radar_1:
    print('carro multado em radar 1')