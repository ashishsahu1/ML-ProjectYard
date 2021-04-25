let videofeed;
let posenet;
let poses = [];
let started = false;
var audio = document.getElementById("audioElement");

// p5.js setup() function to set up the canvas for the web cam video stream
function setup() {
  //creating a canvas by giving the dimensions
  const canvas = createCanvas(500, 500);
  canvas.parent("video");

  videofeed = createCapture(VIDEO);
  videofeed.size(width, height);
  console.log("setup");

  // setting up the poseNet model to feed in the video feed.
  posenet = ml5.poseNet(videofeed);

  posenet.on("pose", function (results) {
    poses = results;
  });

  videofeed.hide();
  noLoop();
}

// p5.js draw function() is called after the setup function
function draw() {
  if (started) {
    image(videofeed, 0, 0, width, height);
    calEyes();
  }
}

// toggle button for starting the video feed
function start() {
  select("#startstop").html("stop");
  document.getElementById("startstop").addEventListener("click", stop);
  started = true;
  loop();
}

// toggle button for ending the video feed
function stop() {
  select("#startstop").html("start");
  document.getElementById("startstop").addEventListener("click", start);
  removeblur();
  started = false;
  noLoop();
}

// defining the parameters used for the posenet : the tracking of the eyes
var rightEye,
  leftEye,
  defaultRightEyePosition = [],
  defaultLeftEyePosition = [];

//function to calculate the position of the various keypoints
function calEyes() {
  for (let i = 0; i < poses.length; i++) {
    let pose = poses[i].pose;
    for (let j = 0; j < pose.keypoints.length; j++) {
      let keypoint = pose.keypoints[j];
      rightEye = pose.keypoints[2].position;
      leftEye = pose.keypoints[1].position;

      // keypoints are the points representing the different joints on the body recognized by posenet

      while (defaultRightEyePosition.length < 1) {
        defaultRightEyePosition.push(rightEye.y);
      }

      while (defaultLeftEyePosition.length < 1) {
        defaultLeftEyePosition.push(leftEye.y);
      }

      // if the current position of the body is too far from the original position blur function is called
      if (Math.abs(rightEye.y - defaultRightEyePosition[0]) > 20) {
        blur();
      }
      if (Math.abs(rightEye.y - defaultRightEyePosition[0]) < 20) {
        removeblur();
      }
    }
  }
}

//function to blur the background and add audio effect
function blur() {
  document.body.style.filter = "blur(5px)";
  document.body.style.transition = "1s";
  var audio = document.getElementById("audioElement");
  console.log("change");
  audio.play();
}

//function to remove the blur effect
function removeblur() {
  document.body.style.filter = "blur(0px)";
  var audio = document.getElementById("audioElement");

  audio.pause();
}
