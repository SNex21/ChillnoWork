let but = document.querySelector("button");

let emlLbl = document.querySelector("#email-label");
let pswLabl = document.querySelector("#password-label");
let emlInp = document.querySelector("#email");
let pswInp = document.querySelector("#password");

document.addEventListener("mouseout", function(){
    if($("#email").is(":focus") || emlInp.value != ""){
        emlLbl.classList.add("activeInputForLable");
    }else{
        emlLbl.classList.remove("activeInputForLable");
    }

    if($("#password").is(":focus") || pswInp.value != ""){
        pswLabl.classList.add("activeInputForLable");
    }else{
        pswLabl.classList.remove("activeInputForLable");
    }
});
document.addEventListener("mouseover", function(){
    if($("#email").is(":focus") || emlInp.value != ""){
        emlLbl.classList.add("activeInputForLable");
    }else{
        emlLbl.classList.remove("activeInputForLable");
    }

    if($("#password").is(":focus") || pswInp.value != ""){
        pswLabl.classList.add("activeInputForLable");
    }else{
        pswLabl.classList.remove("activeInputForLable");
    }
});

// Надо доработать
// pswInp.addEventListener("keydown", function(symb) {
//     if(pswInp.value.length >= 20 && symb.key){
//         symb.preventDefault();
//     }
// });

emlInp.addEventListener("click", function(){
    emlLbl.classList.add("activeInputForLable");

});
pswInp.addEventListener("click", function(){
    pswLabl.classList.add("activeInputForLable");
});

document.addEventListener("keydown", function(event){
	if((['Tab', 'Space'].includes(event.key))){
		event.preventDefault();
    }
});

but.addEventListener("click", function(){
    // let xhr = new XMLHttpRequest();

    // let request = 'email=' + encodeURIComponent(email) + "&password=" + encodeURIComponent(password);
    // xhr.open("POST", 'http://127.0.0.1:8000/user/login', true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.onreadystatechange = function(){
    //     console.log("xer");
    // };
    // xhr.send(request);
    let eml = document.querySelector('#email').value;
    let psw = document.querySelector('#password').value;

    const xhr = new XMLHttpRequest();

    // listen for `load` event

    // create a JSON object
    const json = {
        "email": eml,
        "password": psw
    };
    
    // open request
    xhr.open('POST', 'http://chillnowork.ru/user/login?');
    
    // set `Content-Type` header
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('accept', 'application/json');

    
    // send rquest with JSON payload
    xhr.send(JSON.stringify(json));

    xhr.onload = () => {
    
        // print JSON response

            // parse JSON

        

    if (xhr.status == 200 ){
        xhr.open('POST', 'http://chillnowork.ru/user/id?');
        const json_id = {
            "email": eml,
            "password": psw
        }
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('accept', 'application/json');

    
    // send rquest with JSON payload
        xhr.send(JSON.stringify(json_id));
    
        
    
        window.location.href = "http://chillnowork.ru/";
    }else{
        alert(response['detail']);
    }

}
    
    
    
}
);


