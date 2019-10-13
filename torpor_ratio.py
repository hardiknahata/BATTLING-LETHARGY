from scipy.spatial import distance as dist

def ratio(eye):
	# calculating the euclidean distances between the two sets of
	# vertical eye landmarks
	P = dist.euclidean(eye[1], eye[5])
	Q = dist.euclidean(eye[2], eye[4])

	# calculating the euclidean distance between the horizontal
	# eye landmark
	R = dist.euclidean(eye[0], eye[3])

	# calculating the eye aspect ratio
	eye_ratio = (P + Q) / (2.0 * R)

	return eye_ratio

def mouthratio(mouth):
	A = dist.euclidean(mouth[2],mouth[10])
	B = dist.euclidean(mouth[3],mouth[9])
	C = dist.euclidean(mouth[4],mouth[8])

	D = dist.euclidean(mouth[12],mouth[16])


	mouthdist=(A+B+C) / (3.0)
	return mouthdist

