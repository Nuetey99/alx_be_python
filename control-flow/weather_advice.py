weather_state = input("What's the weather like today? (sunny/rainy/cold)")

if weather_state.lower() == "sunny":
    print ("Wear a t-shirt and sunglasses.")
elif weather_state.lower() == "rainy":
    print ("Don't forget your umbrella and raincoat.")
elif weather_state.lower() == "cold":
    print ("Make sure to wear a warm coat and a scarf.")
else :
    print ("Sorry, i don't have recommendations for this weather.")