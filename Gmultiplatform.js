// Vue.createApp({
//     methods:{
//         post(){
//             console.log("hello world")
//         }
//     }
// })
// console.log(this.msg)




// var myFontSize = document.getElementById(fontselect);
// myFontSize.onclick = function() {
//     console.log(myFontSize.value)
//     body.style.fontSize = myFontSize.value ;
// }

// var myFontSize = document.getElementById(fontinput);
// // var FontSize = myFontSize.value;
// myFontSize.onclick = function() {
//     console.log(myFontSize.value)
//     body.style.fontSize = myFontSize.value ;
// }


var mybody = document.querySelector('body');
var radio1 = document.getElementById("font100")
var radio2 = document.getElementById("font125")
var radio3 = document.getElementById("font150")
var radio4 = document.getElementById("font175")
var radio5 = document.getElementById("font200")

radio1.onclick = function() {
    mybody.className = 'body_class_c1'
}
radio2.onclick = function() {
    mybody.className = 'body_class_c2'
}
radio3.onclick = function() {
    mybody.className = 'body_class_c3'
}
radio4.onclick = function() {
    mybody.className = 'body_class_c4'
}
radio5.onclick = function() {
    mybody.className = 'body_class_c5'
}