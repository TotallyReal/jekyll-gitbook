/**
A simple animation which is invariant under a (translation+reflection) operation on the plane.
For more such patterns, read on Wallpaper groups, for example:
https://en.wikipedia.org/wiki/Wallpaper_group
*/

var triLength = 50;
var s3 = Math.sqrt(3);
var period = 4;
var framesPerLoop = 50;

function setup() {
    triLength = min(windowHeight/3, windowWidth/(period*2-1));
	createCanvas((period*2-1)*triLength, triLength*3);
	background(0);
	//frameRate(5); // slowing the frame rate for the save function below
}


function draw() {
	background(0, 15);
	fill(255);
	text("hello "+windowHeight,50,50);
	translate(0, height/2);
	noStroke();
	for (let i=0; i<2*period; i++){
		push();
			// The big white triangle. Added -1 to Y coordinate, to make it slightly
		  // above the small black triangle
			fill(255);
			rotate((frameCount%framesPerLoop)*Math.PI/framesPerLoop);
			triangle(0, -1, -triLength, -1, -triLength/2, -1-s3*triLength/2);
		
			// The small black triangle.
			translate(-triLength/4,0);
			fill(50);
			triangle(0, 0, -triLength/2, 0, -triLength/4, -s3*triLength/4);
		pop();
		
		// the translation - reflection symmetry.
		translate(triLength,0);
		scale(1,-1);
	}
}