from tamara import Tamara
import face_recognition
import cv2
import time

class FaceDetection():

    def __init__(self):
        self.Tamara = Tamara()
        self.users = self.Tamara.load_db()
        self.online_users = self.Tamara.online()

        self.video_capture = cv2.VideoCapture(0)

        self.me_image = face_recognition.load_image_file("me.jpg")
        self.me_face_encoding = face_recognition.face_encodings(self.me_image)[0]


    def main(self):

        while True:
            #print(self.Tamara.online())

            # Grab a single frame of video
            ret, frame = self.video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces([self.me_face_encoding], face_encoding)
                name = "Unknown"

                if match[0]:
                    self.Tamara.say("Hello Aaron")
                else:
                    print("Not the former president")



        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    x = FaceDetection()
    x.main()
