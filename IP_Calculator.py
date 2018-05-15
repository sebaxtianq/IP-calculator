"""This program validates that an ip address is valid and computes the number of hosts
of the subnetwork and the range of this valid Ip addresses, as well as the broadcast and network IPs"""
import math
def is_valid(ip):
    ip=ip.split(".")
    valids=0
    if len(ip)==4:
        for i in range(len(ip)):
            if ((int(ip[i])>=0) & (int(ip[i])<=255)):
                valids+=1
            else:
                return False
                print ("Valor invalido: "+i)
                break
        if valids==4:
            return True
    else:
        return False
        print ("La IP debe contener 4 octetos")
def to_binary(value):
    try:
        maxim=math.floor(math.log(value,2))
    except:
        maxim=0
    sum=0
    binary=[]
    while True:
        if ((sum+(2**maxim))>value):
            binary.append("0")
        elif ((sum+(2**maxim))<value):
            binary.append("1")
            sum+=2**maxim
        else:
            binary.append("1")
            sum+=2**maxim
            for n in range(maxim):
                binary.append("0")
            break
        maxim-=1
        if (maxim<0 | sum==value):
            break
    return "".join(binary)
def ip_binary(value):
    value=value.split(".")
    for i in range(len(value)):
        value[i]=to_binary(int(value[i]))
        while len(value[i])<8:
            value[i]="0"+value[i]
    return "".join(value)
def valid_mask(mask):
    if is_valid(mask):
        mask=ip_binary(mask)
        lastone=mask.rfind("1")
        firstzero=mask.index("0")
        if lastone<firstzero:
            for i in range(lastone+1):
                if mask[i] == "1":
                    continue
                else:
                    return False
                    break
            for j in range(lastone+1,32):
                if mask[j] == "0":
                    continue
                else:
                    return False
                    break
        else:
            return False
        return True
    else:
        return False
def bin_to_dec(octet):
    pointer=len(octet)-1
    dec=0
    for i in octet:
        dec+=(int(i)*(2**pointer))
        pointer-=1
    return dec
def jump(ip):
    ip=ip_binary(ip)
    zeros=ip.count("0")
    jump=2**zeros
    return jump
ip=input("Ingresar dirección IP: ")
mask=input("Ingresar mascara de subred: ")
binand=[]
if (is_valid(ip) & valid_mask(mask)):
    ip=ip.split(".")
    mask=mask.split(".")
    for i in range(4):
        binand.append(ip_binary(str((int(ip[i]) & int(mask[i])))))
        binand[i]=str(bin_to_dec(binand[i]))
    network=".".join(binand)
    octets=network.split(".")
    if int(octets[3])<255:
        octets[3]=str(int(octets[3])+1)
    elif int(octets[2])<255:
        octets[2]=str(int(octets[2]+1))
    elif int(octets[1])<255:
        octets[1]=str(int(octets[1]+1))
    else:
        octets[0]=str(int(octets[0]+1))
    print ("Network: "+network)
    firsthost=".".join(octets)
    print("Firsthost: "+firsthost)
    binip=ip_binary(network)
    decip=bin_to_dec(binip)
    jump=jump(".".join(mask))
    print (jump)
    decip+=(jump-2)
    binip=to_binary(decip)
    while len(binip)<32:
        binip="0"+binip
    lasthost=[]
    lasthost.append(str(bin_to_dec(binip[0:8])))
    lasthost.append(str(bin_to_dec(binip[8:16])))
    lasthost.append(str(bin_to_dec(binip[16:24])))
    lasthost.append(str(bin_to_dec(binip[24:32])))
    lasthost=".".join(lasthost)
    print("Lasthost: "+lasthost)



