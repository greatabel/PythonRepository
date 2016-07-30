# pip install future
# pip install protobuf
# pip install pytest
# how to run: python test_measure.py  or  python test_measure.py --inputfile testfile

from __future__ import print_function
import measurement_pb2
import sys
import random
import argparse

def writefile():
    measurement = measurement_pb2.Measurement()
    measurement.side_a = True
    measurement.side_b = False
    mylist = random.sample(range(700), 128)
    # mylist = list(range(1,10))
    measurement.image =  ','.join(str(e) for e in mylist)
    print('#:',measurement)

    try:
        f = open('testfile', 'wb')
        f.write(measurement.SerializeToString())
        myprint = " ".join(hex(ord(n)) for n in measurement.SerializeToString())
        print('@:', myprint)
        f.close()
    except IOError:
        print('could not open file')

def testwrite():
    from cStringIO import StringIO

    s = "00001010110000000000000111010000000101110111110111010010001101110111110111010100010101110111110111010110011101110111110111011000100101110111110111011010101101110111110111011100110101110111110111011110111101110111110111100000000101110111111011100010001101110111111011100100010101110111111011100110011101110111111011101000100101110111111011101010101101110111111011101100110101110111111011101110111101110111111011110000000101110111111111110010001101110111111111110100010101110111111111110110011101110111111111111000100101110111111111111010101101110111111111111100110101110111111111111110111101110111111100000000000110001000000000000010001110001000000000000100010110001000000000000110011110001000000000001000100110001000000000001010101110001000000000001100110110001000000000001110111110001000000000010000000110001000000100010010001110001000000100010100010110001000000100010110011110001000000100011000100110001000000100011010101110001000000100011100110110001000000100011110111110001000000100100000000110001000001000100010001110001000001000100100010110001000001000100110011110001000001000101000100110001000001000101010101110001000001000101100110110001000001000101110111110001000001000110000000110001000001100110010001110001000001100110100010110001000001100110110011110001000001100111000100110001000001100111010101110001000001100111100110110001000001100111110111110001000001101000000000110001000010001000010001110001000010001000100010110001000010001000110011110001000010001001000100110001000010001001010101110001000010001001100110110001000010001001110111110001000010000010000000000010001100000000000"
    sio = StringIO(s)

    f = open('testfile', 'wb')

    while 1:
        # Grab the next 8 bits
        b = sio.read(8)
        # Bail if we hit EOF
        if not b:
            break
        # If we got fewer than 8 bits, pad with zeroes on the right
        if len(b) < 8:
            b = b + '0' * (8 - len(b))
        # Convert to int
        i = int(b, 2)
        # Convert to char
        c = chr(i)
        # Write
        f.write(c)


def readfile(filename):
    try:
        f = open(filename,'rb')
        measurementA = measurement_pb2.Measurement()
        #print('before measurementA=', measurementA)
        filestr = f.read()
        # print("###", filestr)
        measurementA.ParseFromString(filestr)
        #print('after measurementA=', measurementA)
        f.close()
        test_measurement_1(measurementA)
    except IOError:
        print('could not open file')

def test_measurement_1(measurement):
    image = ''.join('{0:08b}'.format(ord(x), 'b') for x in measurement.image)
    sourcearray = []        
    for i in range(0,len(image)/24):
        serial = image[24*i:24*(i+1)]
        a = serial[0:8]
        b = serial[8:16]
        c = serial[16:24]
        sourcearray.append(int(b[4:8]+a,2))
        sourcearray.append(int(c+b[0:4],2))

    assert measurement.side_a == True, "should be True"
    assert measurement.side_b == False, "should be False"
    assert sourcearray == range(2000,2128), "should be 2000~2127"
    print('pass test_measurement_1')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", help="you can input a filename to read from.")
    args = parser.parse_args()
    inputname = 'testfile'
    if args.inputfile:
        inputname = args.inputfile
    writefile()
    # testwrite()
    readfile(inputname)






