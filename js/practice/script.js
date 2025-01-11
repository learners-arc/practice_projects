// console.log(`Hello world`);

// a=window.prompt(`tell me your name`);
// console.log(a)
// window.alert(`your name is saved in console`)

// document.getElementById("myh1").textContent = `Hello ansh`;

// let a = `anshkumar`;
// let b = 18;
// let c = true;
// document.getElementById("1h4").textContent = `Hello my name is ${a}`;
// document.getElementById("2h4").textContent = `my age is ${b}`;
// document.getElementById("3h4").textContent = `is student? ${c}`;

// let n = 10;
// n = n + 1;
// n -= 1;
// n++
// console.log(n);

// const n = 10 + 45 - 74 * 25 * (2 * 1) ** 4;
// console.log(n);

// let n = window.prompt(`how old are you`);
// n = Number(n);
// n += 1;
// console.log(n, typeof n);
// let n = 'ansh';
// let x = 18;
// let y;
// n = Number(n);
// x = String(x);
// y = Boolean(y);
// console.log(n, typeof n);
// console.log(x, typeof x);
// console.log(y, typeof y);

// const PI = 3.14157;
// let radius = window.prompt(`Enter radius`);
// radius = Number(radius);
// circumference = 2 * PI * radius;
// circumference += 1;
// console.log(circumference);

// let username;
// let userage;
// let useremail;
// document.getElementById("subbtn").onclick = function () {
//     username = document.getElementById("nameinp").value;
//     console.log(username);
//     document.getElementById("myh1").textContent = `Hello ${username}`;
//     userage = document.getElementById("ageinp").value;
//     console.log(userage);
//     useremail = document.getElementById("emailinp").value;
//     console.log(useremail);
//     window.alert(`Hello ${username} and your age is ${userage}`);
// }

// const PI = 3.14157;
// let radius;
// document.getElementById("subbtn").onclick = function () {
//     radius = document.getElementById("radinp").value;
//     circumference = 2 * PI * radius;
//     document.getElementById("2h4").textContent=`Your circumference is ${circumference}`
// }

// const incbtn = document.getElementById("incbtn");
// // let decbtn;
// // let resbtn;
// const countlabel = document.getElementById("countlabel");
// let count = 0;
// incbtn.onclick = function () {
//     count++;
//     countlabel.textContent = count;
// }
// // document.getElementById("incbtn").onclick = function () {
// //     count++;
// //     document.getElementById("countlabel").textContent = count;
// // }
// document.getElementById("decbtn").onclick = function () {
//     count--;
//     document.getElementById("countlabel").textContent = count;
// }
// document.getElementById("resbtn").onclick = function () {
//     count=0;
//     document.getElementById("countlabel").textContent = count;
// }


const PI = 3.14157;
let radius;
let area;
let volume;
let circumference;
document.getElementById("subbtn").onclick = function () {
    radius = document.getElementById("radinp").value;
    radius = Number(radius);
    area = PI * radius ** 2;
    volume = (4 / 3) * PI * radius ** 3;
    circumference = 2 * PI * radius;
    switch
}
