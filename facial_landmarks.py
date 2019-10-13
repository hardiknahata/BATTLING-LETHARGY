from collections import OrderedDict

#For dlib’s 68-point facial landmark detector:

def FL():

	FACIAL_LANDMARKS_68_IDXS = OrderedDict([
		("mouth", (48, 68)),
		("inner_mouth", (60, 68)),
		("right_eyebrow", (17, 22)),
		("left_eyebrow", (22, 27)),
		("right_eye", (36, 42)),
		("left_eye", (42, 48)),
		("nose", (27, 36)),
		("jaw", (0, 17))
	])

	FACIAL_LANDMARKS_IDXS = FACIAL_LANDMARKS_68_IDXS

	return FACIAL_LANDMARKS_IDXS
