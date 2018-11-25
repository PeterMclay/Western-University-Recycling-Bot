from clarifai.rest import ClarifaiApp, Image as ClImage

app = ClarifaiApp(api_key='eed14e2c7ef140448d7d1b0305d9b19c')

def recyclable(image_url):
    model = app.models.get('recycleOrNot')
    image = ClImage(url=image_url)
    response_data = model.predict([image])
    concepts = response_data['outputs'][0]['data']['concepts']
    concept_names = [concept['name'] for concept in concepts]
    concept_values = [concept['value'] for concept in concepts]
    print(concept_names)
    print(concept_values)
    # largestIndex = 0
    # maxVal = 0
    # for i in range(largestIndex):
    #   if concept_values[i] > maxVal:
    #       largestIndex = i
    #       maxVal = concept_values[i]
    obj = concept_names[0]
    if concept_values[0] < 0.10:
        if obj == "bottles":
            obj = "bottle"
        elif obj == "plastic":
            obj = "plastic container"
        elif obj == "cans":
            obj = "can"
        elif obj == "metalContainers":
            obj = "aluminum container"
        elif obj == "paperContainers":
            obj = "paper container"
        elif obj == "cardboard":
            obj = "cardboard box"
        elif obj == "styrofoamB":
            obj = "styrofoam"
        elif obj == "batteriesB":
            obj = "battery"
        else:
            obj = "electronic device"

        if obj == "bottle" or obj == "plastic container" or obj == "can" or obj == "aluminum container" \
                or obj == "paper container" or obj == "cardboard box" or obj == "paper":
            valx = "👋 Hi, thank you for using the Western University Recycle Bot 🤖! Unfortunately we are not certain what "\
             "the object you sent us is; however, we think it may be a " + obj + ". If that's the case, you ♻ CAN " \
             "RECYCLE ♻ this!!! We are constantly trying to improve our bot and will use this feedback in order to " \
             "improve the results in the future! 🤓"
            return valx
        else:
            valy = "👋 Hi, thank you for using the Western University Recycle Bot 🤖! Unfortunately we are not certain what "\
             "the object you sent us is; however, we think it may be a " + obj + ". If that's the case, you 😢 CAN'T " \
             "RECYCLALE 😢 this!!! We are constantly trying to improve our bot and will use this feedback in order to"\
             " improve the results in the future! 🤓"
            return valy

    elif obj == "bottles" or obj == "plastic" or obj == "cans" or obj == "metalContainers" or obj == "paperContainers" \
            or obj == "cardboard" or obj == "paper":
        if obj == "bottles":
            obj = "bottle"
        elif obj == "plastic":
            obj = "plastic container"
        elif obj == "cans":
            obj = "can"
        elif obj == "metalContainers":
            obj = "aluminum container"
        elif obj =="paperContainers":
            obj = "paper container"
        elif obj == "cardboard":
            obj = "cardboard box"
        else:
            obj = "paper"

        strng = "👋 Hi, thank you for using the Western University Recycle Bot 🤖! It looks like you sent us a picture of a "+\
                obj + ". You ♻ CAN RECYCLE ♻ this!!! Thank you for checking! 👍"
        return strng

    else:
        if obj == "styrofoamB":
            obj = "styrofoam"
        elif obj == "batteriesB":
            obj = "battery"
        else:
            obj = "electronic device"

        stng2 = "👋 Hi, thank you for using the Western University Recycle Bot 🤖! It looks like you sent us a picture of " \
                "a " + obj + ". You 😢 CAN'T RECYCLE 😢 this!!! Thank you for checking! 👍"
        return stng2
