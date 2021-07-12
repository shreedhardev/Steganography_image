from stegano import lsb
img = "file path"
new_img = "hiden.png"
msg = "type your message"

#to hide message
lsb.hide(image,message=msg).save(new_img)

#to reveal the image
message = lsb.reveal(new_img)
print("Hidden message:",message)