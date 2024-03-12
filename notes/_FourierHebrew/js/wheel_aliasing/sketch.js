let size = 0;
let angle = 0;
let N = 16;

function setup() {
    size = min(windowWidth, windowHeight);
    createCanvas(size, size);
    background(100);

    slider = createSlider(0, 100, 10);
    slider.position(10, 10);
    slider.style('width', '80px');
}

function draw() {
	background(0);

	let val = slider.value();
	speed = 10*val/100;
	angle += speed*deltaTime/1000;
	stroke(255);
	strokeWeight(1);
	textAlign(CENTER, CENTER);
	text(""+speed, 30, 40);

	translate(size/2, size/2);

	noFill();
	stroke(255);
	strokeWeight(10);
	circle(0, 0, size-10);
	for (let i=0; i<N; i++){
		line(0, 0, size*cos(angle + 2*PI*i/N)/2, size*sin(angle + 2*PI*i/N)/2);
	}
}