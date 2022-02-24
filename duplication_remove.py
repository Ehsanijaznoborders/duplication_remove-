from PIL import Image
import glob
import hashlib
for img in glob.glob("/home/patient/Downloads/26-April-Mon(Style-ehsan)-20210427T082747Z-001/26-April-Mon_Style-ehsan/*"):
    md5hash = hashlib.md5(Image.open(img).tobytes())
    hsh=md5hash.hexdigest()
    image=Image.open(img)
    image.save("/home/patient/Downloads/26-April-Mon(Style-ehsan)-20210427T082747Z-001/1/"+str(hsh)+".jpg")
