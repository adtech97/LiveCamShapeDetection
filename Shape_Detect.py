#               FINAL                  #
########################################
#   Aadesh Rasal And Pranav Bawiskar   #
#             26/09/2017               #
#  WITHOUT USING CANNY EDGE DETECTION  #
########################################


import cv2
import numpy as np
cap  = cv2.VideoCapture(0)
print("Press q to exit")
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    #read the frames
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #we wont use Guassian blur - reason -> it distorts the threshold image generated later to be processed with blob

    #blob detetection
    detector = cv2.SimpleBlobDetector()
    #ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if ret == True:
        ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        #Keypoints
        kp = detector.detect(thresh)

        #Blobing
        blob = cv2.drawKeypoints(thresh, kp, np.array([]), 255, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        #Finding the Contours
        contour,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contour:

            #contour Approximations to reduce the noise
            app = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

            #Print output as triangle ,square according to length of approximation
            print(len(app))
            if len(app) == 3:
                M = cv2.moments(cnt)

                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0


                print("Triangle")
                cv2.drawContours(blob,[cnt],0,(255,255,255),3)
                cv2.circle(gray, (cX, cY), 7, (255, 255, 255), -1)
                cv2.putText(gray, "TRI", (cX - 20, cY - 20), font, 0.7, (255, 255, 0), 2)
            #Print
            elif len (app) ==5:
                P = cv2.moments(cnt)

                if P["m00"] != 0:
                    pX = int(P["m10"] / P["m00"])
                    pY = int(P["m01"] / P["m00"])
                else:
                    pX, pY = 0, 0

                print("Pentagon")
                cv2.drawContours(blob,[cnt],0,(255,255,255),3)
                cv2.circle(gray, (pX, pY), 7, (255, 255, 255), -1)
                cv2.putText(gray, "PENT", (pX - 20, pY - 20), font, 0.7, (255, 255, 0), 2)


            elif len(app) in range(15,20):
                R = cv2.moments(cnt)

                if R["m00"] != 0:
                    rX = int(R["m10"] / R["m00"])
                    rY = int(R["m01"] / R["m00"])
                else:
                    rX, rY = 0, 0

                print("Circle")
                cv2.drawContours(gray,[cnt],0,(255,255,255),3)
                cv2.circle(gray, (rX, rY), 7, (255, 255, 255), -1)
                cv2.putText(gray, "CIRCLE", (rX - 20, rY - 20), font, 0.7, (255, 255, 0), 2)

            elif len(app) == 10:
                HC = cv2.moments(cnt)

                if HC["m00"] != 0:
                    hcX = int(HC["m10"] / HC["m00"])
                    hcY = int(HC["m01"] / HC["m00"])
                else:
                    hcX, hcY = 0, 0

                print("Half-circle")
                cv2.drawContours(blob,[cnt],0,(255,255,255),3)
                cv2.circle(gray, (hcX, hcY), 7, (255, 255, 255), -1)
                cv2.putText(gray, "H-CIRCLE", (hcX - 20, hcY - 20), font, 0.7, (255, 255, 0), 2)

            elif len (app) == 6:
                HX = cv2.moments(cnt)

                if HX["m00"] != 0:
                    hxX = int(HX["m10"] / HX["m00"])
                    hxY = int(HX["m01"] / HX["m00"])
                else:
                    hxX, hxY = 0, 0

                print("Hexagon")
                cv2.drawContours(blob,[cnt],0,(255,255,255),3)
                cv2.circle(gray, (hxX, hxY), 7, (255, 255, 255), -1)
                cv2.putText(gray, "HEX", (hxX - 20, hxY - 20), font, 0.7, (255, 255, 0), 2)

            elif len(app) == 4:
                (x,y,w,h) = cv2.boundingRect(app)
                ar = w/float(h)
                if ar>=0.90 and ar<=1.10:
                    S = cv2.moments(cnt)

                    if S["m00"] != 0:
                        sX = int(S["m10"] / S["m00"])
                        sY = int(S["m01"] / S["m00"])
                    else:
                        sX, sY = 0, 0

                    print("Square")
                    cv2.drawContours(blob, [cnt], 0, (255, 255, 255), 1)
                    cv2.circle(gray, (sX, sY), 7, (255, 255, 255), -1)
                    cv2.putText(gray, "SQR", (sX - 20, sY - 20), font, 0.7, (255, 255, 0), 2)

                else:
                    RC = cv2.moments(cnt)
                    if RC["m00"] != 0:
                        rcX = int(RC["m10"] / RC["m00"])
                        rcY = int(RC["m01"] / RC["m00"])
                    else:
                        rcX, rcY = 0, 0

                    print("RECT")
                    cv2.drawContours(blob, [cnt], 0, (255, 255, 255), 1)
                    cv2.circle(gray, (rcX, rcY), 7, (255, 255, 255), -1)
                    cv2.putText(gray, "REC", (rcX - 50, rcY - 50), font, 0.7, (255, 255, 0), 2)



    cv2.imshow("result",gray)


    if cv2.waitKey(1) == 1048698:
        break
cap.release()
cv2.destroyAllWindows()
