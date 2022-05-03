from PIL import Image

for i in range(0,415079):
    str_i = str(i)  
    file_name = "contempt/"+str_i+".jpg"   
    
    try:
        img = Image.open(file_name)
        print(f"read {str_i}.jpg")        
        new_width  = 128
        new_height = 128
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        save_name = "resize_128/"+str_i+".jpg"
        img.save(save_name)
        
    except:
       pass
