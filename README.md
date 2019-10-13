Inspiration
According to the Association For Safe International Road Travel along with few other global surveys, there are more than 1.3 million accidents recorded every year, which implies every month on average more than 100,000 lives are lost. In-spite of major enhancements in technology, we still witness such casualties because of irresponsible driving such as being drowsy, distracted, drunk and many more. We identified the necessity of a cost-effective technological model which can prevent accidents and also be accessible from low to middle class sections of the society.

What it does
Our prototype is a creative, compact and cost-effective solution which can seamlessly prevent dangerous accidents in commute by intelligently alerting the driver in lethargy and distraction using Computer Vision.

How we built it
We have used a facial landmark detector to identify facial features in order to extract eye and mouth regions, which are the main identifiers for a driver to be lethargic and distracted respectively. A couple of major libraries namely dlib and open-cv in python are used to build our solution.

Challenges we ran into
Distance between the upper and lower regions of eye is used as a parameter for assessing lethargy. Distance between upper and lower lip is used as a parameter for distraction (continuous speaking or such). Calculation of above statistical parameter that is distance, in order to get the eye-ratio and mouth-ratio was a daunting task.

Accomplishments that we're proud of
We have successfully accomplished the working prototype of our intention, along with nullifying the challenges we faced for parameters extraction without using any sensor.

What we learned
We have explored the realms of computer vision and realized how the similar thought-process can be extended to other use-cases which could be very fruitful.

What's next for BATTLING LETHARGY & DISTRACTION DURING COMMUTE
We plan to deploy the complete prototype on a single-board computer like ORDOID XU4 and make a portable and commercially viable product.

Built With
c++
dlib
numpy
odroid
opencv
playsound
python
