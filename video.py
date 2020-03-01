"""
2020
streamer -q -c /dev/video0 -f rgb24 -r 15 -t 00:00:00 -o ~/outfile.avi /time Model
julian Guillermo zapata rugeles
"""
import os ; import time
complemento=os.popen("pwd").read()
complemento=complemento[:-1] ; complemento=complemento+"/videoStatic/" # ---- reemplace videoStatic for your own folder -----
comand="streamer -q -c /dev/video0 -f rgb24 -r 12 -t 00:00:58 -o "+complemento
cero=0 #counter while cicle

def detectIntall():
        # if packcage is installed , next
        # not : try to install using apt
        status=os.popen("dpkg -s streamer").read()
        if "install ok installed" in status:
            print("installed ... Next ")
        else:
            print("no found  ...installing")
            os.system("sudo apt-get install streamer")
        print("validation pass")

detectIntall()
while cero < 300: # change this interval 300 using N files outputs
    date=os.popen("date").read()
    date=date[:-1];date=date.replace(" ","");date=date+".avi" #file name output
    comandoFull=comand+date
    #print(comandoFull) # uncomment here to show "full comand"
    os.system(comandoFull)
    time.sleep(2)
    cero=cero+1
