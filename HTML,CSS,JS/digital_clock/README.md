# Digital Clock

### This is a simple and stylish digital clock built using HTML, CSS, and JavaScript. The clock updates every second and displays the current time in hours, minutes, and seconds. It features a smooth animation for the labels and has a visually appealing gradient background.

## Features

* Real-time Clock: Displays the current time in hours, minutes, and seconds.
* Custom Animation: The time labels change color smoothly, creating an animated effect.
* Responsive Layout: The clock is centered on the screen and adapts to different screen sizes.
* Modern Design: A gradient background and stylish font give the clock a modern and appealing look.

## How It Works

* HTML Structure:
The HTML creates a simple structure with span elements for displaying hours, minutes, and seconds.
The clock is wrapped in a container that is centered on the screen.
* CSS Styling:
The background uses a linear gradient, and the time is displayed in large, bold text with a shadow effect.
The clock container has a dynamic design with rounded corners and a gradient background.
The clock labels (HOURS, MINUTES, and SECONDS) change color using a keyframe animation.
* JavaScript Functionality:
A JavaScript function clock() retrieves the current time from the system and updates the display every second.
The time is formatted with leading zeros if necessary (e.g., 08 instead of 8 for hours).
The setInterval() method is used to call the clock() function every 1000 milliseconds (1 second).


## Files

* index.html: The HTML structure for the digital clock.
* style.css: The CSS file that provides styling and animations for the clock.
* script.js: JavaScript code that updates the time every second.

