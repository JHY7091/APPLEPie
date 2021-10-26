#변수
#좋아하는 음식을 소개 해주세요
food = "감자탕"
taste = "시원한맛"
ie = "고기"
number = 3 
number_times = number >= 2 

print ("제가 좋아하는 음식은 " + food + " 이예요")
print (food + "는 " + taste +" 이며, " + ie + " 가아주 맛있어요")
print (food + "을 먹으러 1주일에 " + str(number) + "번은 가요 많이 가는 편일까요?" + str(number_times))
# 정수, 참 / 거짓은 + 을 포함한 프린트에서 사용하기 위해서는 str() 로 감싸준다.

print ("제가 좋아하는 음식은 " + food + " 이예요")
print (food + "는 " + taste +" 이며, " + ie + " 가아주 맛있어요")
print (food , "을 먹으러 1주일에 " , number , "번은 가요 많이 가는 편일까요?" , number_times)
# + 대신하여 , 를 사용 시에는 str() 해주지 않아도 괜찮다.