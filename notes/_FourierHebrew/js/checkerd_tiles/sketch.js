let N = 50;
let size = 0;

function setup() {
	size = min(windowWidth, windowHeight);
	createCanvas(size, size);

	slider = createSlider(20, 50, 50);
	slider.position(10, 10);
	slider.style('width', '80px');
	
}

function draw() {
	background(0);
	let resolution = slider.value();
	
	let d = size/resolution;
	
	for (let i=0; i<resolution; i++){
		for (let j=0; j<resolution; j++){
			let x = N*(i+0.5)/resolution;
			let y = N*(j+0.5)/resolution;
			let parity = (floor(x)+floor(y))%2;
			fill(255 * parity);
			stroke(255 * parity);
			rect(i*d, j*d, d,d);
		}
	}
	
	fill(0);
	stroke(255);
	strokeWeight(2);
	textAlign(CENTER, CENTER);
	textSize(30);
	text(""+resolution, 30, 40);
}