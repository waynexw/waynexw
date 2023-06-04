var canvas;
var context;
var width = 400;
var height = 400;
var trans = 220; //canvas.height / 2;
var radius = trans * 0.90;

function animateFrame(time) {
canvas = document.getElementById('myCanvas');
context = canvas.getContext('2d');
context.clearRect(0, 0, 2048, 1536);
context.translate(trans, trans); //jeremyjia fixed
drawClock();
context.translate(-trans, -trans); //jeremyjia fixed
}

function drawClock() {
drawFace(ctx, radius);
drawNumbers(ctx, radius);
drawTime(ctx, radius);
}

function drawFace(ctx, radius) {
var grad;
ctx.beginPath();
ctx.arc(0, 0, radius, 0, 2Math.PI);
ctx.fillStyle = 'white';
ctx.fill();
grad = ctx.createRadialGradient(0,0,radius0.95, 0,0,radius1.05);
grad.addColorStop(0, '#333');
grad.addColorStop(0.5, 'white');
grad.addColorStop(1, '#333');
ctx.strokeStyle = grad;
ctx.lineWidth = radius0.1;
ctx.stroke();
ctx.beginPath();
ctx.arc(0, 0, radius0.1, 0, 2Math.PI);
ctx.fillStyle = '#333';
ctx.fill();
}

function drawNumbers(ctx, radius) {
var ang;
var num;
ctx.font = "30px arial";
ctx.textBaseline="middle";
ctx.textAlign="center";
for(num = 1; num < 13; num++){
ang = num * Math.PI / 6;
ctx.rotate(ang);
ctx.translate(0, -radius0.85);
ctx.rotate(-ang);
ctx.fillText(num.toString(), 0, 0);
ctx.rotate(ang);
ctx.translate(0, radius0.85);
ctx.rotate(-ang);
}
}

function drawTime(ctx, radius){
var now = new Date();
var hour = now.getHours();
var minute = now.getMinutes();
var second = now.getSeconds();
//hour
hour=hour%12;
hour=(hourMath.PI/6)+
(minuteMath.PI/(660))+
(secondMath.PI/(36060));
drawHand(ctx, hour, radius0.5, radius0.07);
//minute
minute=(minuteMath.PI/30)+(secondMath.PI/(3060));
drawHand(ctx, minute, radius0.8, radius0.07);
// second
second=(secondMath.PI/30);
drawHand(ctx, second, radius0.9, radius*0.02);
}

function drawHand(ctx, pos, length, width) {
ctx.beginPath();
ctx.lineWidth = width;
ctx.lineCap = "round";
ctx.moveTo(0,0);
ctx.rotate(pos);
ctx.lineTo(0, -length);
ctx.stroke();
ctx.rotate(-pos);
}
