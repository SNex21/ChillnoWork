

let emlLbl = document.querySelector("#email-label");
let pswLbl = document.querySelector("#password-label");
let cdLbl = document.querySelector("#code-label");
let emlInp = document.querySelector("#email");
let pswInp = document.querySelector("#password");
let cdInp = document.querySelector("#code");
let but = document.querySelector("#loginBut");

console.log(emlInp);

document.addEventListener("mouseout", function(){
    if($("#email").is(":focus") || emlInp.value != ""){
        emlLbl.classList.add("activeInputForLable");
    }else{
        emlLbl.classList.remove("activeInputForLable");
    }

    if($("#password").is(":focus") || pswInp.value != ""){
        pswLbl.classList.add("activeInputForLable");
    }else{
        pswLbl.classList.remove("activeInputForLable");
    }


});
document.addEventListener("mouseover", function(){
    if($("#email").is(":focus") || emlInp.value != ""){
        emlLbl.classList.add("activeInputForLable");
    }else{
        emlLbl.classList.remove("activeInputForLable");
    }

    if($("#password").is(":focus") || pswInp.value != ""){
        pswLbl.classList.add("activeInputForLable");
    }else{
        pswLbl.classList.remove("activeInputForLable");
    }

});

emlInp.addEventListener("click", function(){
    emlLbl.classList.add("activeInputForLable");

});
pswInp.addEventListener("click", function(){
    pswLbl.classList.add("activeInputForLable");
});


// Надо доработать
// pswInp.addEventListener("keydown", function(symb) {
//     if(pswInp.value.length >= 20 && symb.key){
//         symb.preventDefault();
//     }
// });







but.addEventListener("click", function(){
    // let xhr = new XMLHttpRequest();

    // let request = 'email=' + encodeURIComponent(email) + "&password=" + encodeURIComponent(password);
    // xhr.open("POST", 'http://127.0.0.1:8000/user/login', true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.onreadystatechange = function(){
    //     console.log("xer");
    // };
    // xhr.send(request);
    let eml = emlInp.value;
    let psw = pswInp.value;

    const xhr = new XMLHttpRequest();

    // listen for `load` event

    // create a JSON object
    const json = {
        "email": eml,
        "password": psw
    };
    
    // open request
    xhr.open('POST', 'http://chillnowork.ru/user/signup?');
    
    // set `Content-Type` header
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('accept', 'application/json');

    
    // send rquest with JSON payload
    xhr.send(JSON.stringify(json));

    xhr.onload = () => {
        
    
    if (xhr.status == 200){
        window.location.href = "http://chillnowork.ru/";
    }

};
    
    
    }

);
