from manim import *
import math
import random
import re
class VectorArrow(Scene):
    zerodir = MathTex(r"|0 \rangle")
    onedir = MathTex(r"|1 \rangle")
    plusdir = MathTex(r"|+ \rangle")
    minusdir = MathTex(r"|- \rangle")
    plusdirlong = MathTex(r"\frac{|0 \rangle + |1 \rangle}{\sqrt{2}}")
    minusdirlong = MathTex(r"\frac{|0 \rangle + |1 \rangle}{\sqrt{2}}")
    def makeDotGroup(self,x_input):
        d1 = Dot(color=BLUE)
        d2 = Dot(color=BLUE)
        statetext = self.zerodir
        dg = VGroup(d1,d2).arrange(DOWN,buff=2.5)
        l1 = Line(d1.get_center(),d2.get_center()).set_color(BLUE)
        x = ValueTracker(x_input)
        y = ValueTracker(-1.5)
        statetext.next_to(d1,UP)
        statetext.add_updater(lambda z:z.set_x(x.get_value()))
        d1.add_updater(lambda z:z.set_x(x.get_value()))
        d2.add_updater(lambda z:z.set_x(x.get_value()))
        l1.add_updater(lambda z: z.become(Line(d1.get_center(),d2.get_center())))
        self.add(statetext,d1,d2,l1)
        return (statetext,d1,d2,l1,x)
    def moveDotGroup(self,d1,d2,l1,x,xval,statetext,state):
        self.play(x.animate.set_value(xval))
        self.play(FadeOut(statetext))
        #self.remove(statetext)
        statetext = state
        statetext.next_to(d1,UP)
        statetext.add_updater(lambda z:z.set_x(x.get_value()))
        self.play(FadeIn(statetext))
        self.wait(2)
        return statetext
        #self.text = 
        #self.wait(0.5)
    def removeDotGroup(self,d1,d2,l1,statetext):
        self.remove(d1,d2,l1,statetext)
    def construct(self):
        skipcirqs = False
        """
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)

        """
        randbitlenchoice = input("Would you like to use a random bit string length?")
        bitlen = 0
        if randbitlenchoice == "Y" or randbitlenchoice == "y" or randbitlenchoice == "yes":
       	    bitlen	= random.randint(5,18) 
        else:
            bitlen = ord(input("Enter number of bits in Alice's string: "))    
        randbitchoice = input("Would you like to use a random bit string?")
        bits = []
        if randbitchoice == "Y" or randbitchoice == "y" or randbitchoice == "yes":
            for i in range(bitlen):
                if bool(random.getrandbits(1)):
                    bits.append(1)
                else:
                    bits.append(0)
        else:
            val = input("Enter bit string of 0s and/or 1s)")
            for i in range(bitlen):
                if val[i] == "1":
                    bits.append(1)
                elif val[i] == "0":
                    bits.append(0)
        bittext = Tex("Alice's bit string: " + str(bits))
        self.play(Create(bittext))
        randbasischoice = input("Would you like to use a random basis string?")
        basis = []
        if randbasischoice == "Y" or randbasischoice == "y" or randbasischoice == "yes":
            for i in range(bitlen):
                if bool(random.getrandbits(1)):
                    basis.append(1)
                else:
                    basis.append(0)
        else:
            val = input("Enter bit string of 0s and/or 1s)")
            for i in range(bitlen):
                if val[i] == "1":
                    basis.append(1)
                elif val[i] == "0":
                    basis.append(0) 
        basistext = Tex("Alice's basis string: " + str(basis))
        basistext.next_to(bittext,DOWN)
        if not skipcirqs:
            flags = [False,False,False,False]
            self.play(Create(basistext))
            for i in range(len(bits)):
                if bits[i] == 0 and basis[i] == 0:
                    flags[0] = True
                elif bits[i] == 0 and basis[i] == 1:
                    flags[1] = True
                elif bits[i] == 1 and basis[i] == 0:
                    flags[2] = True
                elif bits[i] == 1 and basis[i] == 1:
                    flags[3] = True
                if (all(i for i in flags)):
                    break
            #print("flags: " + str(flags))
            ###Creating Quantum circuit representations
            ##Considering
            flagtext = [None]*4
            cirqs = [None]*4
            if flags[0]==True:
                flagtext[0] = (Tex("Considering alice's bit and basis are both 0 and Bob guesses right"))
                cirqs[0] = ImageMobject("./imgs/qc0.png")
                flagtext[0].next_to(cirqs[0],UP)
            if flags[1] == True:
                flagtext[1] = (Tex("Considering alice's bit is 1 and basis is 0 and Bob guesses right"))
                cirqs[1] = ImageMobject("./imgs/qc1.png")
                flagtext[1].next_to(cirqs[1],UP)
            if flags[2] == True:
                flagtext[2] = (Tex("Considering alice's bit is 0 and basis is 1 and Bob guesses right"))
                cirqs[2] = ImageMobject("./imgs/qc2.png")
                flagtext[2].next_to(cirqs[2],UP)
            if flags[3] == True:
                flagtext[3] = (Tex("Considering alice's bit is 0 and basis is 1 and Bob guesses right"))
                cirqs[3] = ImageMobject("./imgs/qc3.png")
                flagtext[3].next_to(cirqs[3],UP)
            flag = False
            for i in range(len(flagtext)):
                if flagtext[i]!=None:
                    if flag == False:
                        flag = True
                        basistext.next_to(flagtext[i],UP)
                        bittext.next_to(basistext,UP)
                    self.play(Create(flagtext[i]))
                    self.add(cirqs[i])
                    if i == 0:
                        (statetext,d1,d2,l1,x) = self.makeDotGroup(-0.5)
                        statetext = self.moveDotGroup(d1,d2,l1,x,0.5,statetext,self.zerodir)
                        self.removeDotGroup(d1,d2,l1,statetext)
                    if i == 1:
                        (statetext,d1,d2,l1,x) = self.makeDotGroup(-2)
                        #self.play(x.animate.set_value(1.5))
                        statetext = self.moveDotGroup(d1,d2,l1,x,0,statetext,self.onedir)
                        statetext = self.moveDotGroup(d1,d2,l1,x,1.5,statetext,self.zerodir)
                        self.removeDotGroup(d1,d2,l1,statetext)
                    if i == 2:
                        (statetext,d1,d2,l1,x) = self.makeDotGroup(-2)
                        #self.play(x.animate.set_value(1.5))
                        statetext = self.moveDotGroup(d1,d2,l1,x,0,statetext,self.plusdirlong)
                        statetext = self.moveDotGroup(d1,d2,l1,x,1.5,statetext,self.zerodir)
                        self.removeDotGroup(d1,d2,l1,statetext)
                    if i == 3:
                        (statetext,d1,d2,l1,x) = self.makeDotGroup(-3)
                        #self.play(x.animate.set_value(1.5))
                        statetext = self.moveDotGroup(d1,d2,l1,x,-1.5,statetext,self.onedir)
                        statetext = self.moveDotGroup(d1,d2,l1,x,0,statetext,self.minusdirlong)
                        statetext = self.moveDotGroup(d1,d2,l1,x,1.5,statetext,self.onedir)
                        statetext = self.moveDotGroup(d1,d2,l1,x,2.5,statetext,self.zerodir)
                        self.removeDotGroup(d1,d2,l1,statetext)
                    self.wait(1)
                    self.play(FadeOut(flagtext[i]))
                    self.remove(cirqs[i])
        self.remove(bittext)
        bobbasis = []
        luckexp = 0
        superlucky = False
        for i in range(len(bits)):
            if random.getrandbits(int(math.pow(2,luckexp))) > 0 or superlucky == True:
                bobbasis.append(basis[i])
            else:
                bobbasis.append(random.getrandbits(1))
        #print(len(bobbasis)==len(basis))
        bobbasistext = Tex("Bob's basis string: " + str(bobbasis))
        basistext.next_to(ORIGIN,UP)
        bobbasistext.next_to(basistext,DOWN)
        self.play(FadeIn(basistext),FadeIn(bobbasistext))
        count = 0
        i = 0
        fixedbasis = []
        for i in range(len(bobbasis)):
            if bobbasis[i]==basis[i]:
                fixedbasis.append(bobbasis[i])  
        fixedbasistext= Tex("Decided basis string: " + str(fixedbasis))
        fixedbasistext.next_to(bobbasistext,DOWN)
        self.play(FadeIn(fixedbasistext))
        seq = []
        for i in (range(len(fixedbasis)//3)):
            seq.append(random.randint(0,len(fixedbasis)))
        seq.sort()
        sharecheckseqText= Tex("Alice and Bob check bit sequence:" + str(seq))
        self.play(FadeOut(basistext),FadeOut(bobbasistext),FadeOut(fixedbasistext))
        self.play(FadeIn(sharecheckseqText))
        seq.sort(reverse=True)
        print(seq)
        for i in seq:
            fixedbasis.pop(i)
        finalBitText = Tex("If checkbits are the same, the key is:" + str(fixedbasis))
        finalBitText.next_to(sharecheckseqText,DOWN)
        self.play(FadeIn(finalBitText))
        """
        ax = Axes(
        	x_length = 2,
        	y_length = 2,
        	x_range = [-1,1,1],
        	y_range = [-1,1,1],
        	tips = True
        	)
        plane = NumberPlane(
        	x_range	= [-1,1],
        	y_range = [-1,1])
        zerovec = Vector([1,0])
        onevec = Vector([0,1])
        plusvec = Vector([1/math.sqrt(2),1/math.sqrt(2)])
        minusvec = Vector([-1/math.sqrt(2),1/math.sqrt(2)])
        zerodir = MathTex(r"|0 \rangle")
        onedir = MathTex(r"|1 \rangle")
        plusdir = MathTex(r"|+ \rangle")
        minusdir = MathTex(r"|- \rangle")
        zerodir.next_to(zerovec.tip, RIGHT)
        onedir.next_to(onevec.tip, RIGHT)
        plusdir.next_to(plusvec.tip, RIGHT)
        minusdir.next_to(minusvec.tip, LEFT)
        bittext.move_to(DOWN*2)
        basistext.next_to(bittext,DOWN)
        
        self.play(Create(plane),Create(zerovec),Create(onevec),Create(plusvec),Create(minusvec))
        self.play(Create(zerodir),Create(onedir),Create(plusdir),Create(minusdir))
        """

        #self.add(onedir)
        #self.add(plusdir)
        #self.add(minusdir)
        #self.add(numberplane, dot, arrow, origin_text, tip_text)